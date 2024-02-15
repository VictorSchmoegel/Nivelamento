import pandas as pd
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Carregar os dados das operadoras
df = pd.read_csv("./Relatorio_cadop.csv", sep=";", encoding="latin1")
operadoras = df.to_dict(orient="records")


class Item(BaseModel):
    termo: str


@router.post("/busca")
def buscar_operadoras(item: Item):
    termo_busca = item.termo.lower()
    resultado = [
        operadora
        for operadora in operadoras
        if termo_busca in str(operadora["Registro_ANS"])
    ]
    return resultado
