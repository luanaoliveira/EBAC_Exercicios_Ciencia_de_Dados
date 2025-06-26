import pandas as pd

pd.set_option('display.width', None)
df = pd.read_csv('clientes.csv')

# Remover dados
df.drop(labels='pais', axis=1, inplace=True) # Coluna
df.drop(labels=3, axis=0, inplace=True) # linha

# Normalizar campos de texto
df['name'] = df['name'].str.title() # Primeira letra de cada palavra vai ser escrita por letra maiúscula
df['address'] = df['address'].str.lower() # As letras fica tudo minúscula
df['state'] = df['state'].str.strip().str.upper() # Remove espaço em branco e depois converte todas as letras em maiúscula

# Converter tipos de dados
df['age'] = df['age'].astype(int)

# # Tratar valores nulos (ausentes)
# df_fillna = df.fillna(0) # Substituir valores nulos por 0
# df_dropna = df.dropna() # Remover registro com valores nulos
# df_dropna4 = df.dropna(thresh=4)
# df = df.dropna(subset=['cpf'])  # remover registro com cpf nulo

print('Valores nulos:\n', df.isnull().sum())
# print('Quantidade de registros nulos com fillna: ', df_fillna.isnull().sum().sum())
# print('Quantidade de registros nulos com dropna: ', df_dropna.isnull().sum().sum())
# print('Quantidade de registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())
# print('Quantidade de registros nulos com CPF: ', df.isnull().sum().sum())

df.fillna(value={'state': 'Desconhecido'}, inplace=True)
df['address'] = df['address'].fillna('Endereço não informado')
df['corrected_age'] = df['age'].fillna(df['age'].mean)

# Tratar formtao de dados
df['corrected_date'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print(df)

# Tratar dados duplicados
print('Quantidade registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Quantidade registros removendo as duplicadas: ', len(df))

print('Dados Limpos:\n', df)

# Salvar dataframe
df['data'] = df['corrected_date']
df['age'] = df['corrected_age']

# print(df)

df_save = df[['name', 'cpf', 'age', 'data', 'address', 'state']]
df_save.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))

