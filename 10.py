Leia um vetor de 20 inteiros e atribua 0 para todos os elementos que possuírem valores negativos.

vetor=[]
for i in range(20):
    num=int(input())
    if num <= 0:
        vetor.append(0)
    else:
        vetor.append(num)
        
        
for j in vetor:
    print(j)
       
