minhas_pizzas = ['carne de panela', 'quatro queijos', 'alcatra']
for pizza in minhas_pizzas :
    print('Eu gosto de pizza de ' + pizza)
print('Eu realmente gosto de pizzas')

amigo_pizzas = minhas_pizzas[:]
amigo_pizzas.append('cinco queijos')
print('Minhas pizzas favoritas são:\n')
for pizza in minhas_pizzas:
    print(pizza)
print('\nAs pizzas favoritas do meu amigo:\n')
for pizza in amigo_pizzas:
    print(pizza)