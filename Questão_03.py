lista1 = []
lista2 = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if e == 0:
        break
    lista1.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if e == 0:
        break
    lista2.append(e)
lista3 = []
listas = lista1[:]
listas.extend(lista2)
x = 0
while x < len(listas):
    y = 0
    while y < len(lista3):
        if listas[x] == lista3[y]:
            break
        y = y + 1
    if y == len(lista3):
        lista3.append(listas[x])
    x = x + 1
x = 0
while x < len(lista3):
    print(f"{x}: {lista3[x]}")
    x = x + 1