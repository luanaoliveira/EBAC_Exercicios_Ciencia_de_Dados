import numpy as np
import pandas
import random

import pandas as pd
from faker import Faker

faker = Faker('pt_BR')

personal_data = []

for _ in range(1027):
    name = faker.name()
    cpf = faker.cpf()
    age = random.randint(a=18, b=60)
    data = faker.date_of_birth(minimum_age=age, maximum_age=age).strftime("%d/%m/%Y")
    address = faker.address()
    state = faker.state()
    pais = 'Brasil'

    pessoa = {
        'name': name,
        'cpf': cpf,
        'age': age,
        'data': data,
        'address': address,
        'state': state,
        'pais': pais
    }

    personal_data.append(pessoa)

df_people = pd.DataFrame(personal_data)
print(df_people)

df_people.loc[2] = [np.nan, np.nan, 56, np.nan, np.nan, np.nan, 'Brasil']
df_people.loc[5] = [np.nan, np.nan, 56, np.nan, np.nan, np.nan, 'Brasil']
df_people.loc[6] = [np.nan, np.nan, 56, np.nan, np.nan, np.nan, 'Brasil']
df_people.loc[1021] = ['Carlos Eduardo Gonçalves', np.nan, 56, np.nan, np.nan, np.nan, 'Brasil']
df_people.loc[1022] = ['Carlos Eduardo Gonçalves', np.nan, 56, np.nan, np.nan, np.nan, 'Brasil']
df_people.loc[1023] = ['Carlos Eduardo Gonçalves', np.nan, 56, np.nan, 'Setor Vitor Hugo Pinto, 32\nSão Benedito\n29887089 Cirino / RS', 'Pernambuco', 'Brasil']
df_people.loc[1024] = ['Carlos Eduardo Gonçalves', np.nan, 56, np.nan, 'Setor Vitor Hugo Pinto, 32\nSão Benedito\n29887089 Cirino / RS', 'Pernambuco', 'Brasil']
df_people.loc[1025] = ['Carlos Eduardo Gonçalves', '283.150.794-41', 56, '21/08/1968', 'Setor Vitor Hugo Pinto, 32\nSão Benedito\n29887089 Cirino / RS', 'Pernambuco', 'Brasil']
df_people.loc[1026] = ['Carlos Eduardo Gonçalves', '283.150.794-41', 56, '21/08/1968', 'Setor Vitor Hugo Pinto, 32\nSão Benedito\n29887089 Cirino / RS', 'Pernambuco', 'Brasil']
df_people.loc[1027] = ['Carlos Eduardo Gonçalves', '283.150.794-41', 56, '21/08/1968', 'Setor Vitor Hugo Pinto, 32\nSão Benedito\n29887089 Cirino / RS', 'Pernambuco', 'Brasil']

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df_people.to_string()) # head() tail()

df_people.to_csv('clientes.csv')