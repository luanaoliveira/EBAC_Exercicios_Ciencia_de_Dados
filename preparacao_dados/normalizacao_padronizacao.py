import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df.drop(labels=['data', 'estado', 'nivel_educacao', 'numero_filhos', 'area_atuacao'], axis=1)

print(df.describe())

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização -StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head())

print('MinMaxScaler (De 0 a 1):')
print('Idade - Min {:.4f} Max: {:.4f} Mean:{:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].mean(), df['idadeMinMaxScaler'].std()))
print('Salario - Min {:.4f} Max: {:.4f} Mean:{:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].mean(), df['salarioMinMaxScaler'].std()))

print('\nMinMaxScaler (De -1 a 1):')
print(f"Idade - Min {df['idadeMinMaxScaler_mm'].min():.4f} Max: {df['idadeMinMaxScaler_mm'].max():.4f} Mean:{df['idadeMinMaxScaler_mm'].mean():.4f} Std: {df['idadeMinMaxScaler_mm'].std():.4f}")
print(f"salario - Min {df['salarioMinMaxScaler_mm'].min():.4f} Max: {df['salarioMinMaxScaler_mm'].max():.4f} Mean:{df['salarioMinMaxScaler_mm'].mean():.4f} Std: {df['salarioMinMaxScaler_mm'].std():.4f}")

print('\nStandardScaler (Ajuste a média a 0 e desvio padrão a 1)):')
print(f"Idade - Min {df['idadeStandardScaler'].min():.4f} Max: {df['idadeStandardScaler'].max():.4f} Mean:{df['idadeStandardScaler'].mean():.18f} Std: {df['idadeStandardScaler'].std():.4f}")
print(f"salario - Min {df['salarioStandardScaler'].min():.4f} Max: {df['salarioStandardScaler'].max():.4f} Mean:{df['salarioStandardScaler'].mean():.18f} Std: {df['salarioStandardScaler'].std():.4f}")

print('\nRobustScaler (Ajuste a mediana e IQR)):')
statsIdade = df['idadeRobustScaler'].agg(['min', 'max', 'mean', 'std'])
statsSalario = df['salarioRobustScaler'].agg(['min', 'max', 'mean', 'std'])
print('Idade - Min {:.4f} Max: {:.4f} Mean:{:.4f} Std: {:.4f}'.format(*statsIdade.to_list()))
print('Salário - Min {:.4f} Max: {:.4f} Mean:{:.4f} Std: {:.4f}'.format(*statsSalario.to_list()))