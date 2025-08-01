Faça um programa para ler uma lista de nomes dos alunos de uma turma de até 5 alunos. O programa deve solicitar ao usuário os nomes dos alunos, sempre perguntando se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuário irá indicar um nome que ele deseja verificar se está presente na lista, e o programa deve procurar pelo nome (ou parte deste nome) e, se encontrar, deve exibir na tela o nome completo e o índice do vetor onde está guardado este nome.

alunos = []
i = 0
while i < 5:
    nome = input("Aluno: ")
    alunos.append(nome)
    i += 1
    if i < 5:
        if input("Deseja inserir novo aluno? [S/N] ").upper() != 'S':
            break

pesquisa = input("Aluno para pesquisa: ")

cont = 0
for aluno in alunos:
    if pesquisa.lower() in aluno.lower():
        print(aluno)
        print(cont)
    cont += 1
