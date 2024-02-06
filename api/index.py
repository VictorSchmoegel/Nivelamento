from fastapi import FastAPI
from .rotas import links

app = FastAPI()
app.include_router(links.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
