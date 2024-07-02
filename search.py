import requests
import csv
from bs4 import BeautifulSoup

dados = []

url = "https://www.bing.com/maps?q=industria+quimica+rio+de+janeiro&FORM=HDRSC6&cp=-22.906596%7E-43.36914&lvl=10.6"


response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    resultados = []
    for title_tag in soup.find_all("div"):
        resultados.append(title_tag.text +" ; ")
        dados.append(title_tag.text +" ; ")
        print(title_tag.text +" ; \n")

else:
    print("Erro ao carregar a página:", response.status_code)

nome_arquivo = 'dados.csv'
campos = ['Empresa']

with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(campos)
    escritor.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

