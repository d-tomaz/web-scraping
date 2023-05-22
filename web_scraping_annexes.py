import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and "Anexo" in href:
        links.append(href)

with zipfile.ZipFile("annexes.zip", "w") as zip_file:
    for link in links:
        filename = link.split("/")[-1]
        response = requests.get(link)
        zip_file.writestr(filename, response.content)