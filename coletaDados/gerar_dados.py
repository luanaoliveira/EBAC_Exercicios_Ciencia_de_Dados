import pandas
import random

import pandas as pd
from faker import Faker

faker = Faker('pt_BR')

personal_data = []

for _ in range(10):
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

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df_people.to_string()) # head() tail()

df_people.to_csv('clientes.csv')