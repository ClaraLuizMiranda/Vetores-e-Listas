Leia um vetor com 15 posições. Somar e mostrar os números que são ímpares.

vetor = []
impares=[]
soma=0

for i in range(15):
    num = int(input())
    vetor.append(num)
    
for j in vetor:
    if j % 2 != 0:
        impares.append(j)
        soma+=j
    

print(soma)        
for k in impares:
    print(k)
