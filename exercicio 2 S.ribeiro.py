n1 = (float(input("digite a nota primeiro bimestre:")))  
n2 = (float(input("digite a nota segundo bimestre:")))
n3 = (float(input("digite a nota terceiro bimestre:"))) 
n4 = (float(input("digite a nota quarto bimestre:")))

def calculo(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

media = calculo(n1,n2,n3,n4)

if media >=60:
    print("o aluno foi aprovato") 
elif media >= 40:
    print("o aluno esta de recuperação")
else:  print("o aluno foi reprovado")