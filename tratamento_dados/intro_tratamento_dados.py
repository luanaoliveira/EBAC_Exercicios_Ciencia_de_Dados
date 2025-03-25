import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar os últimos registros
print(df.tail().to_string())

# Verificar linhas e colunas
print('Qtd: ', df.shape)

# Verificar tipos de dados
print('Tipagem: \n', df.dtypes)

# # Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())