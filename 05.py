Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

vetor = []
vetorquadrados = []

for i in range(10):
    num = float(input())
    vetor.append(num)
for numero in vetor:
    quadrado = numero ** 2
    vetorquadrados.append(quadrado)

for num in vetor:
    print(f'{num:.2f}')
for quad in vetorquadrados:
    print(f'{quad:.2f}')
