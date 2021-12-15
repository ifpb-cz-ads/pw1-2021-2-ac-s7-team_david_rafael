T = [-10, -8, 0, 1, 2, 5, -2, -4]
minima = T[0]
maxima = T[0]
soma = 0
for c in T:
    if c < minima:
        minima = c
    if c > maxima:
        maxima = c
    soma = soma + c
print("Temperatura minima: {}".format(minima))
print("Temperatura maxima: {}".format(maxima))
print("A soma das temperaturas é {}".format(soma))