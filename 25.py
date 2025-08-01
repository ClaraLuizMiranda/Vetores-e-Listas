Faça uma função que receba dois vetores. Retorne um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números que estão em qualquer um dos vetores. Esse vetor de retorno não deve conter números repetidos.

def funcao(vetor1, vetor2):
    resultado = []
    for i in vetor1:
        duplicado = False
        for existente in resultado:
            if i == existente:
                duplicado = True
                break
        if not duplicado:
            resultado.append(i)

    for i in vetor2:
        duplicado = False
        for existente in resultado:
            if i == existente:
                duplicado = True
                break
        if not duplicado:
            resultado.append(i)
            
    return resultado

 x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y) 
