aça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, se sim escreva esses valores na tela.

vetor = []
for i in range(10):
    num = int(input())
    vetor.append(num)
     
repetidos = []

for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] == vetor[j]:
            repetidos.append(vetor[i])
if len(repetidos)>0:
    for k in repetidos:
        print(k)
