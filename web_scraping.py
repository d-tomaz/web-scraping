# Importação das bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import zipfile

# Definição da URL a ser acessada
url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

# Realização da requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Criação de um objeto BeautifulSoup para fazer o parse do conteúdo HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Lista para armazenar os links relevantes encontrados na página
links = []

# Iteração pelos elementos <a> encontrados no objeto BeautifulSoup
for link in soup.find_all('a'):
    # Obtenção do atributo 'href' do link
    href = link.get('href')
    # Verificação se o link contém a palavra 'Anexo' em seu URL
    if href and 'Anexo' in href:
        # Adição do link à lista de links relevantes
        links.append(href)

# Criação de um arquivo ZIP para armazenar os anexos baixados
with zipfile.ZipFile('anexos.zip', 'w') as zip_file:
    # Iteração pelos links relevantes encontrados
    for link in links:
        # Extração do nome do arquivo a partir da URL
        filename = link.split('/')[-1]
        # Realização da requisição HTTP para obter o conteúdo do anexo
        response = requests.get(link)
        # Escrita do conteúdo do anexo no arquivo ZIP
        zip_file.writestr(filename, response.content)
