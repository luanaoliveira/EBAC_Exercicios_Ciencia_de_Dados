import requests # Fazer requisições http
from bs4 import BeautifulSoup

print('Requests: ')
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/') # URL do site que queremos fazer a busca
print(response.text[:600]) # Mostra tudo em uma linha

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text,features='html.parser')
print(soup.prettify()[:1000])

