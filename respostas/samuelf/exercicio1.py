aluno = input("digite o nome do aluno: ")
n1 = float(input("digite a primeira nota: ") )
n2 = float (input( "digite a segunda nota: ") )
def calcular_media( nota1, nota2):
    media = (nota1+ nota2) / 2 
    return media 
media_calculada = calcular_media(nota1=n1, nota2=n2)


print(f"o aluno {aluno} obteve a seguinte media: {media_calculada}")