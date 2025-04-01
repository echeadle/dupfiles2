from pydantic import BaseModel

class FileEntry(BaseModel):
    path: str
    hash: str
    size: int
    mtime: float