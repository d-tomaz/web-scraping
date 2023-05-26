import requests  # Importa o módulo requests para fazer requisições HTTP
from bs4 import BeautifulSoup  # Importa a classe BeautifulSoup do módulo bs4 para analisar o HTML
import zipfile  # Importa o módulo zipfile para manipular arquivos compactados em formato ZIP

# Define a URL do site a ser acessado
url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

# Faz uma requisição GET para a URL e armazena a resposta
response = requests.get(url)

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
soup = BeautifulSoup(response.content, 'html.parser')

# Cria uma lista vazia para armazenar os links dos anexos
links = []

# Itera sobre todos os elementos "a" encontrados no conteúdo HTML
for link in soup.find_all('a'):
    # Obtém o valor do atributo href do elemento "a"
    href = link.get('href')

    # Verifica se o atributo href existe e se contém a substring "Anexo"
    if href and 'Anexo' in href:
        # Adiciona o link à lista de links
        links.append(href)

# Abre um arquivo ZIP chamado "anexos.zip" para escrita
with zipfile.ZipFile('anexos.zip', 'w') as zip_file:
    # Itera sobre todos os links na lista de links
    for link in links:
        # Obtém o nome do arquivo dividindo o link pelo caractere "/" e pegando o último item resultante
        filename = link.split('/')[-1]

        # Faz uma requisição GET para o link do anexo
        response = requests.get(link)

        # Escreve o conteúdo da resposta no arquivo ZIP com o nome do arquivo obtido
        zip_file.writestr(filename, response.content)
