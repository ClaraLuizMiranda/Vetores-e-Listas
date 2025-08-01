Faça um programa que preencha um vetor com 12 números reais aleatórios (uniformemente distribuídos no intervalo [-10, 10]), mostre esses números, e calcule a quantidade de números negativos e a soma dos números positivos desse vetor. A entrada para o programa é a semente dos números aleatórios.

import random
vetor=[]
cont=0
soma=0

semente = int(input())
random.seed(semente)


for i in range(12):
    num=random.uniform(-10,10)
    vetor.append(num)
    
    if vetor[i]<0:
        cont+=1
    else:
        soma+=num
        
print(cont)
print(f'{soma:.2f}')
