Faça um programa que receba do usuário um vetor com 10 inteiros. Em seguida deverá ser mostrado na tela o maior e o menor valor desse vetor.

vetor=[]

for i in range(10):
    vetor.append(int(input()))
    
for i in range(len(vetor)):
    if i == 0:
        maior = vetor[i]
        menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]
            
print(maior)
print(menor)
