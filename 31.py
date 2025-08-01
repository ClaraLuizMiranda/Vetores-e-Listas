Digite um nome e imprima quantas letras diferentes tem esse nome.

frase = str(input())
frase = frase.replace("-","")
frase = frase.replace(" ", "")
vetor = []

for letra in frase:
    if letra not in vetor:
        vetor.append(letra)
        
print(len(vetor))        
