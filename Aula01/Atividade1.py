import pandas as pd 

data = {
    'Código do Produto': [1, 2, 3],
    'Produtos': ['Notebook', 'Smartphone', 'Tablet'],
    'Unidades Vendidas': [120, 340, 210],
    'Cor': ['Preto', 'Prata', 'Azul'],
    'Categoria':['Eletrônicos', 'Eletrônicos', 'Eletrônicos'],
    'Preço por Unidade (R$)': [3500.00, 2500.00, 1200.50],
    'Faturamento Total (R$)': [420000.00, 850000.00, 252105.00],
    'Satisfação': ['Alto', 'Muito Alto', 'Médio']
}

df = pd.DataFrame(data)

print(f'\n {df}')


print('\n VARIÁVEIS QUANTITATIVAS')
print(30*'=')


print('\nExibindo Unidades Vendidas: ')
print(df['Unidades Vendidas'])

print('\nExibindo Preço por Unidade (R$): ')
print(df['Preço por Unidade (R$)'])

print('\nExibindo Faturamento Total (R$): ')
print(df['Faturamento Total (R$)'])


print('\n VARIÁVEIS QUALITATIVAS')
print(30*'=')

print('\nExibindo Código do Produto: ')
print(df['Código do Produto'])

print('\nProdutos: ')
print(df['Produtos'])

print('\nCor: ')
print(df['Cor'])

print('\nExibindo Categoria: ')
print(df['Categoria'])

print('\nExibindo Satisfação: ')
print(df['Satisfação'])