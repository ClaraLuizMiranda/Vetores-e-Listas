Faça uma função que receba um vetor e um número inteiro x e retorne os múltiplos do número x que existem no vetor.

def funcao(vetor, x):
    if x == 0:
        return []
    multiplos = []
    for num in vetor:
        if num % x == 0:
            multiplos.append(num)
    return multiplos

x1 = []
for i in range(10):
    x1.append(int(input("")))
x2 = int(input(""))
y = funcao(x1, x2)
print(y)  
