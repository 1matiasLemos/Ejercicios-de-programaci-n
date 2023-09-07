from fastapi import APIRouter
from datetime import date
router = APIRouter(prefix='/a')

@router.get('/')
async def root():
    return {'error':date(2023,2,10)}