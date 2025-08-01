Faça um programa para ler 12 inteiros DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados na ordem que forem sendo lidos, mas caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Exibir na tela o vetor final que foi digitado.

def funcao():
    vetor = []
    i = 0
    while i < 12:
        num = int(input())
        
        existe = 0
        for existente in vetor:
            if num == existente:
                existe = 1
                break
        
        if existe == 1:
            print(f"Numero {num} ja existe, escreva outro")
        else:
            vetor.append(num)
            i += 1
    return vetor

vetor_final = funcao()
print(vetor_final)
