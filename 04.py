Crie um programa que lê 10 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.

lista=[]
for i in range(10):
    num=int(input())
    lista.append(num)
for j in lista[::-1]:
    print(j)
