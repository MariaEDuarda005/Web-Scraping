from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

site = rf"D:\FPOO-Formativa-WebScraping_E-commerce.html"

with open(site, "r", encoding="utf-8") as arquivo:
    conteudo_html = arquivo.read()

# criando o objeto beautiful soup
soup = BeautifulSoup(conteudo_html, "html.parser")

# criando uma variável que armazena o que encontrar de <tabela>
tabela_pedidos = soup.find('table')

pedido = []
numero_pedido = []
data = []
itens = []
quantidade = []
preco_unitario = []
total = []
status = []

# esse [1:] é para ele não pegar o cabeçalho
linhas_tabela = soup.find_all('tr')[1:]

for linha in linhas_tabela:
    colunas = linha.find_all('td')
    numero_pedido.append(colunas[0].text)
    data.append(colunas[1].text)
    itens.append(colunas[2].text)
    quantidade.append(colunas[3].text)
    preco_unitario.append(colunas[4].text)
    total.append(colunas[5].text)
    status.append(colunas[6].text)

# Movido para fora do loop
data_frame = {
    'N° do pedido': numero_pedido,
    'Data': data,
    'Itens': itens,
    'Quantidade': quantidade,
    'Preço Unitário': preco_unitario,
    'Total': total,
    'Status': status
}

df = pd.DataFrame(data_frame)
df.to_excel("Historicos_pedidos.xlsx", index=False)
df.to_json("Historicos_pedidos.json",orient='records', lines=True, force_ascii=False)
df.to_csv("Historicos_pedidos.csv", index=False, encoding='utf-8')
