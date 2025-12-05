#========= ex 1 =========#
for x in range (1, 50 +1, 1):
    print(x)

#========= ex 2 =========#
for x in range (2, 100 +1, 2):
    print(x)

#========= ex 3 =========#
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

media = (n1 + n2 + n3 + n4 + n5)/ 5
print(media)

#========= ex 4 =========#
pt = int(input("Digite o número de tabuada que você quer: "))

tabuada = {
    f"1 x {pt}": int(1*pt),
    f"2 x {pt}": int(2*pt),
    f"3 x {pt}": int(3*pt),
    f"4 x {pt}": int(4*pt),
    f"5 x {pt}": int(5*pt),
    f"6 x {pt}": int(6*pt),
    f"7 x {pt}": int(7*pt),
    f"8 x {pt}": int(8*pt),
    f"9 x {pt}": int(9*pt),
    f"10 x {pt}": int(10*pt)    
}

print(tabuada)

#========= ex 5 =========#
palavra = int(input("Digite uma palavra: ")).lower()
vogais = "aeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print(f"A palavra tem {contador} vogais.")
