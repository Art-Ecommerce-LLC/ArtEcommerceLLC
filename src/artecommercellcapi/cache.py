# src/artecommercellcapi/service.py
from src.artecommercellcapi.repository import SiteContentRepository
from src.artecommercellcapi.datauri import ImageDataUriConverter
from src.artecommercellcapi.models import SiteContentDataUri
from typing import List
from functools import lru_cache
import ast
import asyncio

class Cache:
    def __init__(self):
        self.converter = ImageDataUriConverter()

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_site_content_data_uri_sync() -> List[SiteContentDataUri]:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(Cache._get_site_content_data_uri_async())

    @staticmethod
    async def _get_site_content_data_uri_async() -> List[SiteContentDataUri]:
        site_content = await SiteContentRepository.fetch_all()
        converter = ImageDataUriConverter()

        site_content_data_uri_list = []
        for content in site_content:
            path = ast.literal_eval(content.file)[0]["path"]
            data_uri = converter.convert_paths_to_data_uris([path])[0]

            site_content_data_uri = SiteContentDataUri(
                id=content.id,
                label=content.label,
                created_at=content.created_at,
                updated_at=content.updated_at,
                created_by=content.created_by,
                updated_by=content.updated_by,
                file=content.file,
                file_data_uri=data_uri
            )
            site_content_data_uri_list.append(site_content_data_uri)

        return site_content_data_uri_list

    async def get_site_content_data_uri(self) -> List[SiteContentDataUri]:
        return await asyncio.to_thread(self._get_site_content_data_uri_sync)

    async def get_site_content_data_uri_by_label(self, label: str) -> str:
        site_content_data_uri_list = await self.get_site_content_data_uri()
        for content in site_content_data_uri_list:
            if content.label == label:
                return content.file_data_uri
        return None
