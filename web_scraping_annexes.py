import requests                           # Importa o módulo requests para fazer requisições HTTP
from bs4 import BeautifulSoup             # Importa a classe BeautifulSoup do módulo bs4 para analisar o HTML
import zipfile                            # Importa o módulo zipfile para manipular arquivos compactados em formato ZIP

url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude" # Define a URL do site a ser acessado

response = requests.get(url)              # Faz uma requisição GET para a URL e armazena a resposta
soup = BeautifulSoup(response.content, "html.parser") # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta

links = []                                # Cria uma lista vazia para armazenar os links dos anexos
for link in soup.find_all("a"):           # Itera sobre todos os elementos "a" encontrados no conteúdo HTML
    href = link.get("href")               # Obtém o valor do atributo href do elemento "a"
    if href and "Anexo" in href:          # Verifica se o atributo href existe e se contém a substring "Anexo"
        links.append(href)                # Adiciona o link à lista de links
        
with zipfile.ZipFile("annexes.zip", "w") as zip_file: # Abre um arquivo ZIP chamado "annexes.zip" para escrita
    for link in links:                    # Itera sobre todos os links na lista de links
        filename = link.split("/")[-1]    # Obtém o nome do arquivo dividindo o link pelo caractere "/" e pegando o último item resultante
        response = requests.get(link)     # Faz uma requisição GET para o link do anexo
        zip_file.writestr(filename, response.content) # Escreve o conteúdo da resposta no arquivo ZIP com o nome do arquivo obtido
