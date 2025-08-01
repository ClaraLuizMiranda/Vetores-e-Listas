Faça uma função que receba dois vetores, A e B, de mesmo tamanho. Crie um novo vetor denominado C calculando C = A – B (a diferença elemento a elemento). Retorne o vetor C.

def funcao(A, B):
    C = []
    for i in range(len(A)):
        C.append(A[i] - B[i])
    return C

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)  
