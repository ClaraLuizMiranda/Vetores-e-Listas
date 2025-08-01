Faça uma função que receba dois vetores. Retorne um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Esse vetor de retorno não deve conter números repetidos.

def funcao(v1, v2):
    r = []
    for i in v1:
        if i in v2 and i not in r:
            r.append(i)
    return r

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)
