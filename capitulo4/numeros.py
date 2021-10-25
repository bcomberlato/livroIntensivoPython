for value in range(1,5):
    print(value)
print("\nTrocou de loop\n")
for value in range(1, 6):#Conjunto fechado na origem e aberto no final logo não vai conter o número 6
    print(value)

numeros = list(range(1,5))
print(numeros)

numeros = list(range(2,11,2)) #fazendo listas pulando de 2 em 2
print(numeros)

numeros = list(range(1,11))
quadrados = []
for numero in numeros:
    quadrado = numero**2
    quadrados.append(quadrado)
    print(numero**2)
print(quadrados)
for numero in numeros:
    quadrados.append(numero**2)
    print(numero**2)

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digitos)) #menor valor da lista
print(max(digitos)) #maior valor da lista
print(sum(digitos)) #soma da lista

quadrados = [quadrado**2 for quadrado in range(1,11)]
print (quadrados)
numeros = list(range(1,21))
print(numeros)
for numero in numeros:
    print(numero)
numeros =  list(range(1,1_000_000+1))
#for numero in numeros:
   #print(numero)
print(min(numeros))
print(max(numeros))
print(sum(numeros))
print(list(range(1, 20, 2)))
multiplos_3 = list(range(3, 31, 3))
for numero in multiplos_3:
    print(numero)
cubos = []

cubos = [cubo**3 for cubo in range(1, 11)]
print(cubos)

for cubo in range(1,11):
    cubo = cubo**3
    cubos.append(cubo)
    print(cubo)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
my_foods.append('cannoli')
friends_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
print(numeros[int((len(numeros)/2)-2):int((len(numeros)/2)+1)])
print(numeros[-3:])

