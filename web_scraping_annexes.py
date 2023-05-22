import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")