aluno = input("Digite o nome do aluno: ")
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) /2
    return media



media_calculada = calcular_media(nota1=n1, nota2=n2)

if media_calculada>=60:
    print("Aprovado!")

elif media_calculada>=40:
    print("Recuperação")

else:
    print("Reprovado")


