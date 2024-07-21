# src/artecommercellcapi/datauri.py
import base64
from PIL import Image
from io import BytesIO
import requests
from src.artecommercellcapi.config import NOCODB_PATH
from logging import getLogger
from typing import List

logger = getLogger(__name__)

class ImageDataUriConverter:
    def __init__(self):
        self.base_url = NOCODB_PATH

    def convert_paths_to_data_uris(self, paths: List[str]) -> List[str]:
        try:
            data_uris = []
            for path in paths:
                url_path = f"{self.base_url}/{path}"
                img_data = requests.get(url_path).content
                data_uri = self.convert_to_data_uri(img_data)
                data_uris.append(data_uri)
            logger.info("Converted image paths to data URIs")
            return data_uris
        except Exception as e:
            logger.error(f"Error converting paths to data URIs: {e}")
            raise

    def convert_to_data_uri(self, image_data: bytes) -> str:
        try:
            with Image.open(BytesIO(image_data)) as img:
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                width, height = img.size
                new_size = (int(width * 0.9), int(height * 0.9))
                resized_img = img.resize(new_size, Image.ANTIALIAS)
                buffer = BytesIO()
                resized_img.save(buffer, format="JPEG")
                resized_img_data = buffer.getvalue()
            base64_data = base64.b64encode(resized_img_data).decode('utf-8')
            logger.info("Converted image data to data URI")
            return f"data:image/jpeg;base64,{base64_data}"
        except Exception as e:
            logger.error(f"Error converting image data to data URI: {e}")
            raise
