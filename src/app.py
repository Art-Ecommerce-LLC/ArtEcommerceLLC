# app/main.py
from fastapi import (
    FastAPI, Request, Form, UploadFile, File, HTTPException, Depends
)
from fastapi.responses import ( 
    HTMLResponse, JSONResponse, RedirectResponse
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.artecommercellcapi.database import Database, lifespan
from typing import List
from src.artecommercellcapi.models import Keys, SiteContent, SiteContentDataUri
from src.artecommercellcapi.repository import KeysRepository, SiteContentRepository
from src.artecommercellcapi.middleware import add_middleware
from src.artecommercellcapi.logger import logger
from src.artecommercellcapi.cache import Cache
import os
import time

# Initialize FastAPI App
desc = "Backend platform for Art Ecommerce LLC"

app = FastAPI(
    title="Art Ecommerce LLC API",
    description=desc,
    version="0.1",
    lifespan=lifespan
)

# Add Middleware
add_middleware(app)

# Get path of where the file is running
script_path = os.path.abspath(__file__)

# Get the directory where the script is located
script_dir = os.path.dirname(script_path)

# Static files and templates
static_dir = os.path.join(script_dir, "static")
templates_dir = os.path.join(script_dir, "templates")

# Static files and templates
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

# Cache dependency
def get_cache():
    return Cache()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    # Check a range of errors with one handler
    if 400 <= exc.status_code < 500:
        return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

# @app.get("/keys", response_model=List[Keys])
# async def get_keys(cache: Cache = Depends(get_cache)):
#     try:
#         keys = await KeysRepository.fetch_all()
#         logger.info(f"Keys fetched: {keys}")
#         return keys
#     except Exception as e:
#         logger.error(f"Error fetching keys: {e}")
#         raise HTTPException(status_code=500, detail="Error fetching keys")
    
# @app.get("/sitecontent", response_model=List[SiteContent])
# async def get_site_content(cache: Cache = Depends(get_cache)):
#     try:
#         site_content = await SiteContentRepository.fetch_all()
#         logger.info(f"Site content fetched: {site_content}")
#         return site_content
#     except Exception as e:
#         logger.error(f"Error fetching site content: {e}")
#         raise HTTPException(status_code=500, detail="Error fetching site content")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request, cache: Cache = Depends(get_cache)):
    logger.info(f"Homepage accessed by: {request.client.host}")
    try:
        artecommercelogo = await cache.get_site_content_data_uri_by_label("artecommercelogo")
        artist_logo = await cache.get_site_content_data_uri_by_label("artistlogo")
        herologo = await cache.get_site_content_data_uri_by_label("herologo")
        headerlogo = await cache.get_site_content_data_uri_by_label("headerlogo")
        ceoheadshot = await cache.get_site_content_data_uri_by_label("ceoheadshot")
        briglogo = await cache.get_site_content_data_uri_by_label("briglogo")
        context = {
            "version": str(int(time.time())),
            "artecommercelogo": artecommercelogo,
            "artistlogo": artist_logo,
            "herologo": herologo,
            "headerlogo": headerlogo,
            "ceoheadshot": ceoheadshot,
            "briglogo": briglogo
        }
        return templates.TemplateResponse(request=request, name="index.html", context=context)
    except Exception as e:
        logger.error(f"Error in homepage: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/favicon.ico", response_class=RedirectResponse)
async def favicon(cache: Cache = Depends(get_cache)):
    return RedirectResponse(url="/static/favicon.ico")
