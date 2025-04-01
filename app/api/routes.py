from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Duplicate File Finder API"}