import uvicorn
from fastapi import FastAPI
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from .routers import router

app = FastAPI(title="Прототип терминала")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
def on_startup():
    with engine.begin() as conn:
        Base.metadata.create_all(bind=engine)


if '__main__'==__name__:
    uvicorn.run("main.app", host= "0.0.0.0")