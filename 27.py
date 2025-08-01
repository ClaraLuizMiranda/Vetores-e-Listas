Faça uma função que receba um vetor posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. No final, retorne o vetor compacto.

def funcao(vetor):
    vetor2 = []
    for elemento in vetor:
        if elemento != 0:
            vetor2.append(elemento)
    return vetor2

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)
