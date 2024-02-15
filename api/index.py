from fastapi import FastAPI
from .rotas import links, transformacaoDeDados, testeApi

app = FastAPI()
app.include_router(links.router)
app.include_router(transformacaoDeDados.router)
app.include_router(testeApi.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
