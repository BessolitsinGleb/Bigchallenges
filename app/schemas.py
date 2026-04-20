from pydantic import BaseModel

class FindCells(BaseModel):
    cell_id: str

class AddCont(BaseModel):
    cell_id: str
    value: str