Leia um vetor com 15 posições. Contar e escrever os valores pares desse vetor.

vetor = []
pares=[]


for i in range(15):
    num = int(input())
    vetor.append(num)
    

for j in vetor:
    if j % 2 == 0:
        pares.append(j)
        
print(len(pares))
for k in pares:
    print(k)
