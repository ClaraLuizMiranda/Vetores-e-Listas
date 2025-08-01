Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondente a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

vetor=[]
for i in range(8):
    num=float(input())
    vetor.append(num)
x=int(input())
y=int(input())

soma=vetor[x]+vetor[y]

print(f'{soma:.2f}')
