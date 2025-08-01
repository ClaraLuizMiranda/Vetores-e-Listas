Faça uma função que, dado um vetor de números reais, ordene os elementos desse vetor do maior para o menor, e retorne o vetor ordenado. Não use nenhuma função de ordenação do python.

def funcao(vetor):
    num = len(vetor)
    for i in range(num):
        maior = i
        for j in range(i + 1, num):
            if vetor[j] > vetor[maior]:
                maior = j
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
    return vetor

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)  
