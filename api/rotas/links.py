import requests
from fastapi import APIRouter
from bs4 import BeautifulSoup
from zipfile import ZipFile

router = APIRouter()


@router.post("/links")
def link():
    http_session = requests.Session()
    pdf_filename_anexo01, pdf_filename_anexo02 = baixa_pdf(http_session)
    zipar_pdf(pdf_filename_anexo01, pdf_filename_anexo02)
    return {"message": "PDFs baixados e zipados com sucesso"}


def baixa_pdf(http_session):
    response = http_session.get(
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/"
        + "participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    )
    soup = BeautifulSoup(response.text, "html.parser")
    convert_pdf_link = soup.select(".internal-link")
    pdf_link_anexo01 = convert_pdf_link[0].get("href")
    pdf_link_anexo02 = convert_pdf_link[2].get("href")

    pdf_response = http_session.get(pdf_link_anexo01)
    pdf_response2 = http_session.get(pdf_link_anexo02)
    pdf_filename_anexo01 = pdf_link_anexo01.split("/")[-1]
    pdf_filename_anexo02 = pdf_link_anexo02.split("/")[-1]

    with open(pdf_filename_anexo01, "wb") as f:
        f.write(pdf_response.content)
    with open(pdf_filename_anexo02, "wb") as f:
        f.write(pdf_response2.content)

    return pdf_filename_anexo01, pdf_filename_anexo02


def zipar_pdf(pdf_filename_anexo01, pdf_filename_anexo02):
    # Cria um arquivo zip com o PDF dentro
    with ZipFile("anexos.zip", "w") as zipf:
        zipf.write(pdf_filename_anexo01)
        zipf.write(pdf_filename_anexo02)
