L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite outro valor a procurar:"))
x =0
while x < len(L):
    print("Primeiro valor")
    if p in L:
        index = L.index(p)
        print(f"{p} foi encontrado na Lista")
        x=+1
        break
    else:
        print("valor nao encontrado!")
        break
while x < len(L):
    print("")
    print("Segundo valor:")
    if v in L:
        index2 = L.index(v)
        print(f"{v} foi encontrado na Lista")
        x=+1
        break
    else:
        print("valor não encontrado!")
        break
print("")
if index < index2:
    print(f"O valor {p} foi encontrado primeiro")
else:
    print(f"O valor {v} foi encontrado primeiro") 