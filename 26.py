Faça uma função que receba dois vetores. Retorne um vetor que seja a diferença entre os 2 vetores anteriores, ou seja, que contém os números que estão no primeiro vetor mas não no segundo vetor. Esse vetor de retorno não deve conter números repetidos.

def funcao(vetor1, vetor2):
    result = []
    
    for elemento in vetor1:
        encontrado = 0
        for item in vetor2:
            if item == elemento:
                encontrado = 1
                break
        
        duplicado = 0
        for item in result:
            if item == elemento:
                duplicado = 1
                break
        
        if encontrado == 0 and duplicado == 0:
            result.append(elemento)
    
    return result


x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)
