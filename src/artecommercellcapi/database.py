import psycopg
from psycopg import AsyncConnection
from contextlib import asynccontextmanager
from src.artecommercellcapi.config import POSTGRES_CONNECTION_STRING
from src.artecommercellcapi.constants import TableNames
from typing import List, TypeVar, Type
from pydantic import BaseModel
import asyncio
import logging
from fastapi import FastAPI

T = TypeVar('T', bound=BaseModel)

class Database:
    _conn: AsyncConnection = None

    @classmethod
    async def connect(cls) -> AsyncConnection:
        if cls._conn is None or cls._conn.closed:
            logging.info("Connecting to the database...")
            cls._conn = await psycopg.AsyncConnection.connect(POSTGRES_CONNECTION_STRING)
        return cls._conn

    @classmethod
    async def disconnect(cls) -> None:
        if cls._conn is not None:
            logging.info("Disconnecting from the database...")
            await cls._conn.close()
            cls._conn = None

    @classmethod
    async def reconnect(cls) -> AsyncConnection:
        logging.info("Reconnecting to the database...")
        await cls.disconnect()
        return await cls.connect()

    @classmethod
    async def fetch_all(cls, table_name: str, model: Type[T]) -> List[T]:
        conn = await cls.connect()
        try:
            async with conn.cursor() as cursor:
                await cursor.execute(f"SELECT * FROM {table_name}")
                columns = [desc[0] for desc in cursor.description]
                rows = await cursor.fetchall()
                result = [model(**dict(zip(columns, row))) for row in rows]
            return result
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            await cls.reconnect()
            raise e

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.connect()
    yield
    await Database.disconnect()
