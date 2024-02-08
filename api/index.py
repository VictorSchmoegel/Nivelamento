from fastapi import FastAPI
from .rotas import links, transformacaoDeDados

app = FastAPI()
app.include_router(links.router)
app.include_router(transformacaoDeDados.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
