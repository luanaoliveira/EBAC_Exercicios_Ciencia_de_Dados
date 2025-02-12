import requests # Fazer requisições http
from bs4 import BeautifulSoup # Para parsear (analisar) o HTML

url = 'https://wiki.python.org.br/AprendaMais' # URL da página
request = requests.get(url) # Faz uma requisição GET à URL fornecida para obter o conteúdo da página
extraction = BeautifulSoup(request.text, features='html.parser') # Faz o parsing (análise) do HTML utilizando a biblioteca BeautifulSoup

# Exibir o texto extraído do HTML
print(extraction.text.strip())

# Filtrar a exibição pela tag
for line_text in extraction.find_all('h2'):  # Percorre as tags de <h2>
    title = line_text.text.strip() # Mostra o texto do título de cada <h2>
    print('Título: ', title) # Mostra o txto do título de cada <h2>

# __________________________________________________________________
# Desafio:
# Filtrar tags ['h2', 'p']
# Contar quantos <h2> e <p> existem no documento (linha_texto.name == tag)
# __________________________________________________________________

# Contar quantidade de títulos e parágrafos

# Inicializa contadores para títulos e parágrafos
count_titles = 0
count_paragraphs = 0

#  Percorre todas as tags <h2> e <p>
for line_text in extraction.find_all(['h2', 'p']):
    if line_text.name == 'h2': # Se a tag for <h2>, então incrementa o contador de títulos
        count_titles += 1
    elif line_text.name == 'p': # Se a tag for <p>, então incrementa o contador de parágrafos
        count_paragraphs += 1

# Exibem o texto extraido das tags <h2> e <p>
print(f"Quantidade de títulos: {count_titles}")
print(f"Quantidade de parágrafos: {count_paragraphs}")

# Exibir somente o texto das tags <h2> e <p>
for line_text in extraction.find_all(['h2', 'p']):
    if line_text.name == 'h2': # Se a tag for <h2>, então exibe os textos da tag <h2>
        titles = line_text.text.strip()
        print(f"Título: \n {titles}")
    elif line_text.name == 'p': # Se a tag for <p>, então exibe os textos da tag <p>
        paragraphs = line_text.text.strip()
        print(f"Parágrafo: \n {paragraphs}")

# Exibir tags aninhada: exibir links das tags <a> dentro dos parágrafos <p> que vem após títulos
for title in extraction.find_all('h2'):
    print('\n Título: ', title.text.strip())
    for link in title.find_next_siblings('p'): # Percorre as tags de <p> que vem logo depois de <h2>
        for a in link.find_all('a', href=True): # Percorre as tags <a> que estão dentro das tags de <p>
            print('Texto Link: ', a.text.strip(), ' | URL:', a["href"]) # Mostra os texto que estão no link e em seguida os links

