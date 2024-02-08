import tabula
from fastapi import APIRouter
from zipfile import ZipFile

router = APIRouter()


@router.post("/transformacao")
def lerPdf():
    tables_df = tabula.read_pdf(
        input_path="./meuPdf.pdf", output_format="dataframe", pages="all"
    )
    tables_df = tables_df[0]

    # Renomeando as colunas
    tables_df.rename(
        columns={
            "RN\r(alteração)": "RN (alteração)",
            "OD": "Seg. Odontológica",
            "AMB": "Ambulatorial",
        },
        inplace=True,
    )

    # Exportando o DataFrame para um arquivo CSV
    nome = "Victor Schmoegel"
    csv_filename = f"Teste_{nome}.csv"
    tables_df.to_csv(
        path_or_buf=csv_filename,
        sep=";",
        encoding="utf-8-sig",
        index=False,
        header=True,
    )
    ziparTabelas(csv_filename)
    return {"message": "PDF lido e transformado com sucesso"}


def ziparTabelas(csv_filename):
    nome = "Victor Schmoegel"
    with ZipFile(f"Teste_{nome}.zip", "w") as zipf:
        zipf.write(csv_filename)
    return {"message": "Tabelas zipadas com sucesso"}
