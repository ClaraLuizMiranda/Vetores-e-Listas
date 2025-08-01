Dado um vetor de n elementos, descubra se existem segmentos iguais máximos. Dois segmentos são iguais se seus elementos são iguais, em ordem, e eles são máximos se têm o maior tamanho possível. Determine as posições de início dos segmentos, bem como o tamanho dos segmentos iguais máximos, e imprima esses valores. Por exemplo, no vetor [7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4], o segmento [5, 4, 3] se repete duas vezes, começando nas posições 2 e 6, e o segmento [5, 4] se repete três vezes, começando nas posições 2, 6, e 10, mas o segmento [5, 4, 3] é máximo por que tem maior tamanho. Os segmentos devem ter tamanho pelo menos igual a 2. Não é necessário encontrar todas as ocorrências de segmentos iguais, o programa pode terminar depois que encontrar a primeira ocorrência máxima. Por exemplo, no vetor [7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4, 3], apesar do segmento [5, 4, 3] aparecer três vezes, nas posições 2, 6 e 10, o programa deve retornar apenas que o segmento apareceu nas posições 2 e 6, e que tem tamanho 3. Faça isso em uma função.

def funcao(vetor):
    n = len(vetor)
    maximo = -1
    posicoes = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            tamanho = 0
            while (i + tamanho < n and j + tamanho < n and vetor[i + tamanho] == vetor[j + tamanho]):
                tamanho += 1

            if tamanho >= 2:
                if tamanho > maximo:
                    maximo = tamanho
                    posicoes = [i, j]
    
    if maximo == -1:
        return -1, -1, -1
    else:
        return posicoes[0], posicoes[1], maximo

x = []
for i in range(10):
    x.append(int(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")
