numeros = []
for i in range(5):
    numero = int(input("digite m numero"))
    numeros.append(numero)
    
def maior_numero(lista):
    return max(lista)

print (f"esse é o maior numero {maior_numero(numeros)}")
