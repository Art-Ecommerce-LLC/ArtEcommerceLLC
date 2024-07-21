from src.artecommercellcapi.database import Database
from src.artecommercellcapi.models import Keys, SiteContent
from src.artecommercellcapi.constants import TableNames
from typing import List
import logging

class KeysRepository:
    @classmethod
    async def fetch_all(cls) -> List[Keys]:
        try:
            return await Database.fetch_all(TableNames.keys(), Keys)
        except Exception as e:
            logging.error(f"Error in KeysRepository: {e}")
            # Retry logic
            await Database.reconnect()
            return await Database.fetch_all(TableNames.keys(), Keys)

class SiteContentRepository:
    @classmethod
    async def fetch_all(cls) -> List[SiteContent]:
        try:
            return await Database.fetch_all(TableNames.sitecontent(), SiteContent)
        except Exception as e:
            logging.error(f"Error in SiteContentRepository: {e}")
            # Retry logic
            await Database.reconnect()
            return await Database.fetch_all(TableNames.sitecontent(), SiteContent)
