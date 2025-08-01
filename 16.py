Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os elementos que não aparecem repetidos.

def funcao(vetor):
    nao_repetidos = []

    for i in vetor:
        if vetor.count(i) == 1:
            nao_repetidos.append(i)
            
    return nao_repetidos
    

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)
