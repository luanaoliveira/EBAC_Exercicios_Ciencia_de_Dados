import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option ('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado_civil'
df = pd.concat(objs=[df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
# df = pd.concat(objs=[df, pd.get_dummies(df, columns = ['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataFrame após codificação one-hot para 'estado-civil':\n", df.head())

print(df['nivel_educacao'].unique())

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nDataFrame após codificação ordinal para 'nivel_nivel':\n", df.head())

print(df['area_atuacao'].unique())

# Transformar 'area_atuacao' em categorias codificadas usando o método cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())
print(f"\n Categorias criadas pelo cat.codes: \n {df['area_atuacao'].astype('category')}")
print(df['area_atuacao_cod'])

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataFrame após aplicar LabelEncoder em 'estado':\n", df.head())

print("\nMapeamento entre os valores originais e os códigos:")
for i, estado in enumerate(label_encoder.classes_):
    print(f"{estado} -> {i}")