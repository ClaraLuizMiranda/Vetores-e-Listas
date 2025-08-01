Faça uma função que receba um vetor com as notas de vários alunos, e retorne a média geral, o desvio padrão (populacional), e quantos alunos estão com nota menor que 7.0.

def funcao(notas):
    n = len(notas)
    if n == 0:
        return 0.0, 0.0, 0

    soma = 0
    for nota in notas:
        soma += nota
    media = soma / n

    soma_quadrados = 0
    for nota in notas:
        soma_quadrados += (nota - media)**2
    
    desvio_padrao = (soma_quadrados / n)**0.5

    menorquesete = 0
    for nota in notas:
        if nota < 7.0:
            menorquesete += 1
            
    return media, desvio_padrao, menorquesete

x = []
for i in range(15):
    x.append(float(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3}")
