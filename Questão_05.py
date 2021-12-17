L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
x =0
while x < len(L):
    if p in L:
        index = L.index(p)
        print(f"{p} foi encontrado na Lista")
        x=+1
        break
    else:
        print("valor nao encontrado!")
        break