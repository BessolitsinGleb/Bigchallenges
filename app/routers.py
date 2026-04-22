from fastapi import APIRouter, Depends, HTTPException
from .database import get_db
from sqlalchemy.orm import Session
from .models import Coordinates, Mooving
from sqlalchemy import select, cast, String, update, Float
from .schemas import FindCells, AddCont
from typing import List
from datetime import datetime

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
        raise HTTPException(403, "cell is not empty")
    
    cell = list(cell.cell_id)
    if cell[0] == 'B':
        cell[0] = 'A'
        a_cell = ''.join(cell)

        num = select(Coordinates).where(Coordinates.cell_id == a_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) == 0.0:
            raise HTTPException(403, "there is no support under the cell")
    
    if cell[0] == 'C':
        cell[0] = 'B'
        b_cell = ''.join(cell)

        num = select(Coordinates).where(Coordinates.cell_id == b_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) == 0.0:
            raise HTTPException(403, "there is no support under the cell")
        
    time = Mooving(value= cast(data.value, Float))
    db.add(time)
    
    update_stmt = (
        update(Coordinates)
        .where(Coordinates.cell_id == data.cell_id)
        .values(value=cast(data.value, Float)) 
    )
    
    db.execute(update_stmt)
    db.commit()
    
    return {"status": "success", "cell": data.cell_id, "container": data.value}

@router.get("/check")
def check_cont(
    # type: str,
    cont_num: str,
    db: Session = Depends(get_db)
):
    list_cells = []
    list_conts = []
    cont = select(Coordinates).where(cast(Coordinates.value, String) == cont_num)
    cont = db.execute(cont).scalar_one_or_none()

    if not cont:
        raise HTTPException(404, "not found")
    
    cell = list(cont.cell_id)
    if cell[0] == 'A':
        cell[0] = 'B'
        b_cell = ''.join(cell)
        list_cells.append(b_cell)

        num = select(Coordinates).where(Coordinates.cell_id == b_cell)
        num = db.execute(num).scalar_one_or_none()
        list_conts.append(num.value)

        cell[0] = 'C'
        c_cell = ''.join(cell)
        list_cells.append(c_cell)

        num = select(Coordinates).where(Coordinates.cell_id == c_cell)
        num = db.execute(num).scalar_one_or_none()
        list_conts.append(num.value)

        return list_cells, list_conts
    
    if cell[0] == 'B':

        cell[0] = 'C'
        c_cell = ''.join(cell)
        list_cells.append(c_cell)

        num = select(Coordinates).where(Coordinates.cell_id == c_cell)
        num = db.execute(num).scalar_one_or_none()
        list_conts.append(num.value)

        return list_cells, list_conts
    
    if cell[0] == 'C':
        return "there are no other containers above your container"

@router.get("/find_cont")
def find_cont(cell_id: str,
              db: Session = Depends(get_db)):
    cell = select(Coordinates).where(Coordinates.cell_id == cell_id)
    cell = db.execute(cell).scalar_one_or_none()

    if not cell:
        raise HTTPException(404, "not found")
    
    return {"status": "success", "cont_num": cell.value}

@router.post("/loading")
def load_cont(value: str,
              db: Session = Depends(get_db)):
    stmt = select(Coordinates).where(cast(Coordinates.value, String) == value)
    cont = db.execute(stmt).scalar_one_or_none()

    if not cont:
        raise HTTPException(404, "not found")
    if value == '0':
        raise HTTPException(404, "no")
    
    cell = list(cont.cell_id)
    if cell[0] == 'A':
        cell[0] = 'B'
        b_cell = ''.join(cell)

        num = select(Coordinates).where(Coordinates.cell_id == b_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) != 0.0:
            raise HTTPException(403, "the cell above is not free")
    
    if cell[0] == 'B':
        cell[0] = 'C'
        c_cell = ''.join(cell)

        num = select(Coordinates).where(Coordinates.cell_id == c_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) != 0.0:
            raise HTTPException(403, "the cell above is not free")
        
    res = update(Coordinates).where(cast(Coordinates.value, String) == value).values(value = cast(0, Float))

    time = update(Mooving).where(cast(Mooving.value, String) == value).values(deleted_at = datetime.utcnow())

    db.execute(time)
    db.execute(res)
    db.commit()

    return {"status": "success"}

@router.post("/rearrangement")
def rearrange_cont(value: str,
                   cell: str,
                   db: Session = Depends(get_db)):
    
    stmt = select(Coordinates).where(cast(Coordinates.value, String) == value)
    cell_from = db.execute(stmt).scalar_one_or_none()

    cell_to = select(Coordinates).where(Coordinates.cell_id == cell)
    cell_to = db.execute(cell_to).scalar_one_or_none()

    if not cell_from:
        raise HTTPException(404, "not found")
    if not cell_to:
        raise HTTPException(404, "not found")
    if float(cell_from.value) == 0.0:
        raise HTTPException(403, "cell is empty")
    if float(cell_to.value) != 0.0:
        raise HTTPException(403, "cell is not empty")
    
    cell__ = list(cell_from.cell_id)
    if cell__[0] == 'A':
        cell__[0] = 'B'
        b_cell = ''.join(cell__)

        num = select(Coordinates).where(Coordinates.cell_id == b_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) != 0.0:
            raise HTTPException(403, "the cell above is not free")
    
    if cell__[0] == 'B':
        cell__[0] = 'C'
        c_cell = ''.join(cell__)

        num = select(Coordinates).where(Coordinates.cell_id == c_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) != 0.0:
            raise HTTPException(403, "the cell above is not free")
        
    cell_ = list(cell_to.cell_id)
    if cell_[0] == 'B':
        cell_[0] = 'A'
        a_cell = ''.join(cell_)

        num = select(Coordinates).where(Coordinates.cell_id == a_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) == 0.0:
            raise HTTPException(403, "there is no support under the cell")
    if cell_[0] == 'C':
        cell_[0] = 'B'
        b_cell = ''.join(cell_)

        num = select(Coordinates).where(Coordinates.cell_id == b_cell)
        num = db.execute(num).scalar_one_or_none()
        if float(num.value) == 0.0:
            raise HTTPException(403, "there is no support under the cell")
    
    rearrange_from = update(Coordinates).where(cast(Coordinates.value, String) == value).values(value = cast(0, Float))
    rearrange_to = update(Coordinates).where(Coordinates.cell_id == cell).values(value = cast(value, Float))

    db.execute(rearrange_from)
    db.execute(rearrange_to)
    db.commit()

    return {"status": "success",
            "container": value,
            "from": cell_from.cell_id,
            "to": cell_to.cell_id}

#check_coordinates, check_mooving