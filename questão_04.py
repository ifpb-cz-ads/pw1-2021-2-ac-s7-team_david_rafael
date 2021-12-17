expressão = input("Digite sua expressao: ")
x = 0
L = []
while x < len(expressão):
    if expressão[x] == "(":
        L.append("(")
    if expressão[x] == ")":
        if len(L) > 0:
            topo = L.pop(-1)
        else:
            L.append(")")
            break
    x = x + 1
if len(L) == 0:
    print("Expressao esta correta")
else:
    print("Erro")