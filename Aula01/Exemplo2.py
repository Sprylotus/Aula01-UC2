import os 

os.system('cls')


import pandas as pd 

produtos = ['Tablet', 'Notebook']
quant_estoque = 30, 15

estoque = pd.Series(quant_estoque, index=produtos)

print('Série Estoque de Produtos:')
print(estoque)

print('\nEstoque de Tablet e Notebook')
print(estoque[['Tablet', 'Notebook']].values)


print('\nProdutos com estoque abaixo de 20 unidades:')
print(estoque[estoque < 20])

print('\nAumentando o estoque em 5 unidades para todos os produtos:')
print(estoque + 5)


estoque.loc['Headphone'] = None
print('\nEstoque com valor nulo (Headphone):')
print(estoque)


precos = pd.Series([1200, 2500], index=produtos)

print('\nValor total do estoque por produto (preço * quantidade):')
print(precos * estoque)