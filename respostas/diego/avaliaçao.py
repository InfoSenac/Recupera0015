alunos = []
notas = []

for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)
    
    for i in range(3):
        nota = float(input("Digite a nota: "))
        notas.append(nota)

print(alunos)
print(notas)


def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) /3
    return media


for i, nota in enumerate(notas):
    print(i, nota)
    #media_calculada = calcular_media(nota)
    #print(media_calculada)




# [aluno1[nota1, nota2 ,nota3], aluno2[nota1, nota2 ,nota3], aluno3[nota1, nota2 ,nota3], aluno4[nota1, nota2 ,nota3], aluno5[nota1, nota2 ,nota3]]

