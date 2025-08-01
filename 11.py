Faça um programa para ler a nota de 15 alunos e armazene em um vetor, calcule e imprima a média geral.

vetor=[]
soma=0
for i in range(15):
    nota=float(input())
    vetor.append(nota)
    soma+=vetor[i]
    media=soma/15
print(f'{media:.2f}')
        
