import uvicorn
from fastapi import FastAPI
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Прототип терминала")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if '__main__'==__name__:
    uvicorn.run("main.app", host= "0.0.0.0")