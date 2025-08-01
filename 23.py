Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.


def primo(num):
    
    if num == 0 or num == 1 or num == -1:
        return False
   
    num = abs(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

vetor = []
for i in range(10):
    num2 = int(input())
    vetor.append(num2)

for i in range(len(vetor)):
    if primo(vetor[i]):
        print(vetor[i])
        print(i)
