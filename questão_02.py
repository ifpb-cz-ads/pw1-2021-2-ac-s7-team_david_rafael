L1 = []
while True:
    n = int(input("Digite um numero para a primeira lista (0 para sair): "))  
    if n == 0:
        break
    L1.append(n)

L2 = []
while True:
    n = int(input("Digite um numero para a segunda lista (0 para sair)"))
    if n == 0:
        break
    L2.append(n)
    
L3 = L1
L3.extend(L2)
x = 0
while x < len(L3):
    print(L3[x])
    x = x + 1

