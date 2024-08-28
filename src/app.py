# app/main.py
from fastapi import (
    FastAPI, Request, Form, UploadFile, File, HTTPException, Depends
)
from fastapi.responses import ( 
    HTMLResponse, JSONResponse, RedirectResponse
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.artecommercellcapi.database import lifespan
from typing import List
from src.artecommercellcapi.middleware import add_middleware, limiter
from src.artecommercellcapi.logger import logger
# from src.artecommercellcapi.cache import Cache
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



@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    # Check a range of errors with one handler
    if 400 <= exc.status_code < 500:
        return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)



@app.get("/", response_class=HTMLResponse, name="index")
@limiter.limit("100/minute")
async def homepage(request: Request):
    logger.info(f"Homepage accessed by: {request.client.host}")
    try:
        context = {
            "version": str(int(time.time())),
        }
        return templates.TemplateResponse(request=request, name="index.html", context=context)
    except Exception as e:
        logger.error(f"Error in homepage: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/about", response_class=HTMLResponse, name="about")
@limiter.limit("100/minute")
async def about_page(request: Request):
    logger.info(f"About page accessed by: {request.client.host}")
    try:
        context = {
            "version": str(int(time.time()))
        }
        return templates.TemplateResponse(request=request, name="about.html", context=context)
    except Exception as e:
        logger.error(f"Error in about page: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/contact", response_class=HTMLResponse, name="contact")
@limiter.limit("100/minute")
async def contact_page(request: Request):
    logger.info(f"Contact page accessed by: {request.client.host}")
    try:
        context = {
            "version": str(int(time.time()))
        }
        return templates.TemplateResponse(request=request, name="contact.html", context=context)
    except Exception as e:
        logger.error(f"Error in contact page: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/community", response_class=HTMLResponse, name="community")
@limiter.limit("100/minute")
async def community_page(request: Request):
    logger.info(f"Community page accessed by: {request.client.host}")
    try:
        context = {
            "version": str(int(time.time()))
        }
        return templates.TemplateResponse(request=request, name="community.html", context=context)
    except Exception as e:
        logger.error(f"Error in community page: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/pricing", response_class=HTMLResponse, name="pricing")
@limiter.limit("100/minute")
async def pricing_page(request: Request):
    logger.info(f"Pricing page accessed by: {request.client.host}")
    try:
        context = {
            "version": str(int(time.time()))
        }
        return templates.TemplateResponse(request=request, name="pricing.html", context=context)
    except Exception as e:
        logger.error(f"Error in pricing page: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/favicon.ico", response_class=RedirectResponse)
async def favicon(request: Request):
    return RedirectResponse(url="/static/favicon.ico")