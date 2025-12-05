
#========= ex 1 =========#
nm = float(input("Digite um número: "))

if ( nm > 0):
    print("positivo")
elif (nm < 0):
    print("negativo")
elif ( nm == 0):
    print("zero")

#========= ex 2 =========#
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if (n1 > n2):
    print(n1)
elif (n1 < n2):
    print(n2)
elif (n1 == n2):
    print("iguais")

#========= ex 3 =========#
idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#========= ex 4 =========#
nota = float(input("Digite uma nota de 0 à 10: "))

if (nota < 5):
    print("Reprovado")
elif (5 <= nota< 7):
    print("Recuperação")
else:
    print("Aprovado")