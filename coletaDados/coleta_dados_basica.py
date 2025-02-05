import requests # Fazer requisições http

response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/') # URL do site que queremos fazer a busca
print(response.text[:600]) # Mostra tudo em uma linha

# Entendimento do código

texto = 'Extrair mensagem de texto'

subtexto = texto[:16]
print(subtexto) # Extrair mensagem

subtexto = texto[8:]
print(subtexto) # mensagem de texto

subtexto = texto[-5:]
print(subtexto) # texto

subtexto = texto[:-5]
print(subtexto) # Extrair mensagem de

# _________________________________________________________________

texto2 = list(range(1,20))

subtexto = texto2[:16]
print(subtexto) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

subtexto = texto2[8:]
print(subtexto) # [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

subtexto = texto2[-5:]
print(subtexto) # [15, 16, 17, 18, 19]

subtexto = texto2[:-5]
print(subtexto) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]