Faça uma função que receba dois vetores de mesmo tamanho e calcule outro vetor contendo, nas posições pares o valores do primeiro vetor e nas posições ímpares os valores do segundo vetor.

def funcao(a, b):
    c = []
    for i in range(len(a) * 2):
        if i % 2 == 0:
            c.append(a[i // 2])
        else:
            c.append(b[i // 2])
    return c

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)
