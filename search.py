import requests
import csv
from bs4 import BeautifulSoup

dados = []
# Defina o URL da página que você deseja pesquisar
url = "https://www.bing.com/maps?q=industria+quimica+rio+de+janeiro&FORM=HDRSC6&cp=-22.906596%7E-43.36914&lvl=10.6"

# Faça uma solicitação HTTP para o URL
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Parseie o conteúdo HTML usando o BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontre as tags <title> e adicione o conteúdo ao array
    resultados = []
    for title_tag in soup.find_all("div"):
        resultados.append(title_tag.text +" ; ")
        dados.append(title_tag.text +" ; ")
        print(title_tag.text +" ; \n")

    # Agora, 'resultados' contém os títulos encontrados na página

else:
    print("Erro ao carregar a página:", response.status_code)

nome_arquivo = 'dados.csv'
campos = ['Empresa']

# Dados fictícios


# Crie o arquivo CSV e escreva os dados
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(campos)
    escritor.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

