Faça uma uma função que receba um vetor com a nota de 15 alunos e e retorne tanto a média geral quanto o desvio padrão (populacional).

def funcao(x):  
    media = soma = 0   
    for c in range(len(x)): 
        media += x[c]   
    media = media/15 
    for c in range(len(x)): 
        x[c] = x[c]-media   
        x[c] = x[c]**2  
        soma += x[c]    
    soma = soma/15   
    return media,soma**(1/2) 


 = []
for i in range(15):
    x.append(float(input("")))
y1, y2 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
