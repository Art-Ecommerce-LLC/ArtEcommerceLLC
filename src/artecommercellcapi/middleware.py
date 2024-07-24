# app/middleware.py
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi import FastAPI
from src.artecommercellcapi.config import MIDDLEWARE_STRING
import os
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

origin = os.getenv("origin")

# Initialize the Limiter
limiter = Limiter(key_func=get_remote_address)

def add_middleware(app : FastAPI) -> None:
    # Session Middleware

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
