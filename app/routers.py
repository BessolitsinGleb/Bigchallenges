from fastapi import APIRouter, Depends, HTTPException
from .database import get_db
from sqlalchemy.orm import Session
from .models import Coordinates
from sqlalchemy import select, cast, String, update, Float
from .schemas import FindCells, AddCont
from typing import List

router = APIRouter(prefix="/container", tags=['container'])

@router.get("/find_cells", response_model=List[FindCells])
def find_cells(
    value: str,
    db: Session = Depends(get_db)
):
    list_ = select(Coordinates).where(cast(Coordinates.value, String) == str(value))

    values = db.execute(list_)
    res = values.scalars().all()
    return res

@router.post("/add")
def add_cont(
    data: AddCont,
    db: Session = Depends(get_db)
):
    stmt = select(Coordinates).where(Coordinates.cell_id == data.cell_id)
    cell = db.execute(stmt).scalar_one_or_none()

    if not cell:
        raise HTTPException(404, detail="not found")
    
    if float(cell.value) != 0.0:
        raise HTTPException(403, "cell isnt empty")
    
    update_stmt = (
        update(Coordinates)
        .where(Coordinates.cell_id == data.cell_id)
        .values(value=cast(data.value, Float)) 
    )
    
    db.execute(update_stmt)
    db.commit()
    
    return {"status": "success", "cell": data.cell_id, "container": data.value}