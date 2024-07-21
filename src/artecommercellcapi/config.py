# app/config.py
import dotenv
import os
# Get file path of .env file
dotenv_path = dotenv.find_dotenv()

# Load environment variables from .env file
dotenv.load_dotenv(dotenv_path)

# Get environment variables
NOCODB_PATH = os.getenv("nocodb_path")
NOCODB_XC_TOKEN = os.getenv("nocodb_xc_token")

# Get table strings
KEY_TABLE = os.getenv("keys")
SITE_CONTENT_TABLE = os.getenv("site_content")

# PostgreSQL connection string
POSTGRES_CONNECTION_STRING = os.getenv("postgres_connection_string")

# Middleware string
MIDDLEWARE_STRING = os.getenv("middleware_string")