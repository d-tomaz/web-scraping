import requests
from bs4 import BeautifulSoup
import zipfile

# Definição da URL
url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

# Requisição da página
response = requests.get(url)

# Criação de um objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Localização dos links dos anexos
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and "Anexo" in href:
        links.append(href)

# Criação do arquivo zip
with zipfile.ZipFile("annexes.zip", "w") as zip_file:
    for link in links:
        # Obtém o nome do arquivo do link
        filename = link.split("/")[-1]
        
        # Requisição do link do anexo
        response = requests.get(link)
        
        # Escreve o conteúdo no arquivo zip
        zip_file.writestr(filename, response.content)