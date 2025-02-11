import requests # Fazer requisições http
from bs4 import BeautifulSoup  # Para parsear (analisar) o HTML
import pandas as pd # Manipulação de dados em tabelas

# Requisição HTTP para obter o HTML da página
print('Requests:  ')
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/') # Faz uma requisição GET à URL fornecida
print(response.text[:600]) # Retorna os primieros 600 caracteres do HTML retornado

# Uso do BeautifulSoup para analisar o HTML
print('BeautifulSoup: ')
soup = BeautifulSoup(response.text,features='html.parser') # Faz o parsing do HTML usando o BeautifulSoup
print(soup.prettify()[:1000]) # Exibe os primeiros 1000 caracteres do HTML formatado

#  Tentativa de extrair tabela usando o pandas
print("Pandas: ")
url_dados = pd.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/') # Tenta extrair tabelas da página
print(url_dados[0].head(5)) # Exibe as primeiras 5 linhas da primeira tabela encontrada

#  Não foi possível extrair a tabela porque a página carrega os dados da tabela dinamicamente via JavaScript e o pandas.read_html() só
#  consegue extrair tabelas que estão no HTML estático