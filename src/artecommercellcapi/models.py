# src/artecommercellcapi/models.py
from pydantic import BaseModel
from datetime import datetime
from dataclasses import dataclass

class SiteContent(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str
    file: str

class Keys(BaseModel):
    id: int
    envval: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str
    envvar: str

@dataclass
class SiteContentDataUri:
    id: int
    label: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str
    file: str
    file_data_uri: str
