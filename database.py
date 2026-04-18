import numpy as np
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

data = np.random.uniform(0, 100, (3, 30, 3))

layers = ['A', 'B', 'C']
coords = ['X', 'Y', 'Z']
rows = []

for i, layer in enumerate(layers):
    for j in range(30):
        for k, coord in enumerate(coords):
            cell_id = f"{layer}{coord}{j+1}"
            value = data[i, j, k]
            rows.append([cell_id, layer, j+1, coord, value])
            
engine = create_async_engine("postgresql+asyncpg://aleksejbessolicin:password@localhost:5432/terminal", echo = True)

df = pd.DataFrame(rows, columns=['cell_id', 'layer', 'row_num', 'coord_type', 'value'])
df.to_sql('container_storage', engine, if_exists='replace', index=False)

print("Данные успешно загружены в PostgreSQL!")

async_session = async_sessionmaker(engine, expire_on_commit= False, class_= AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session