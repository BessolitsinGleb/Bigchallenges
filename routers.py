from fastapi import APIRouter

router = APIRouter(prefix="/container", tags=['container'])

@router.post("/add")
def q():
    pass