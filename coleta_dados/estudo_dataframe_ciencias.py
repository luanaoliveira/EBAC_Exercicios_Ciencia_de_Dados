# Estudo Dataframe
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Ana', 'Marcos', 'Carlos']
print(f'Lista de nomes: \n {lista_nomes}')
print(f'Primeiro Elemento da lista: {lista_nomes[0]}')

# Dicionário: Estrutura composta de pares chave-valor
dicionario_pessoa = {
    # 'nome': 'Ana',
    'idade': '20',
    'cidade': 'São Paulo'
}

print(f'Dicionário de uma pessoa: \n {dicionario_pessoa}')
print(f'Atributo do Dicionário: \n {dicionario_pessoa.get('nome', 'Não informado')}')

# Listas de dicionários: Estrutura de dados que combina listas e dicionários
dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'São Paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'São José dos Campos'},
    {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio de Janeiro'}
]

# DataFrame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n', df)

# Selecionar coluna
print(df['nome'])

# Selecionar várias colunas
print(df[['nome', 'idade']])

# Selecionar linhas pelo o índice
print('Primeira linha \n', df.iloc[0])

# Adicionar uma nova coluna
df['salario'] = [4100, 3600, 5200]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Taubaté',
    'salario': 4800
}

df.loc[len(df)] = ['Jamile', 32, 'Juazeiro', 6000] # Adiciona um novo registro
df.loc[2] = ['Jam', 31, 'Taubaté', 5000] # Adiciona um novo registro na posição 2

print(f'DataFrame Atual \n {df}')

# Removendo uma coluna
df.drop(labels='salario', axis=1, inplace=True)

# Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >= 30]
print(f'Filtro \n {filtro_idade}')

# Salvando o DataFrame em arquivo CSV
df.to_csv(path_or_buf='dados.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print(f'\n Leitura do CSV \n {df_lido}')