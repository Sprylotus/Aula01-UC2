import pandas as pd 

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],
    'Gênero': ['F','M','F'],
    'Altura': [1.70, 1.80, 1.65]
}

df = pd.DataFrame(data)


print(f'\n {df}')

print('Exibindo Idade: ')
print(df['Idade'])

print('Exibindo Altura: ')
print(df['Altura'])

print('Exibindo Gênero: ')
print(df["Gênero"])