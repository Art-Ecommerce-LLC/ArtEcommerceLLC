# app/middleware.py
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi import FastAPI
from src.artecommercellcapi.config import MIDDLEWARE_STRING
import os

origin = os.getenv("origin")

def add_middleware(app : FastAPI) -> None:
    # Session Middleware
    app.add_middleware(
        SessionMiddleware, 
        secret_key=MIDDLEWARE_STRING,
        )
    
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
