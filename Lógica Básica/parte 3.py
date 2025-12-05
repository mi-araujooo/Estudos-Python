#========= ex 1 =========#
lista = [1, 5, 8, 10, 5, 8 ,9, 45, 65]
contagem = 0
for x in lista:
    contagem+= x
print(contagem)

#========= ex 2 =========#
lista = [1, 5, 8, 10, 5, 8 ,9, 45, 65]
maior = lista[0]

for x in lista:
    if(x > maior):
        maior = x
print(maior)

#========= ex 3 =========#
lista = [1, 5, 8, 10, 5, 8 ,9, 45, 65]
lista_nova = []

for x in lista:
    if (x >= 10):
        lista_nova.append(x)
print(lista_nova)

#========= ex 4 =========#
lista = [1, 5, 8, 10, 5, 8 ,9, 45, 65]
lista_inv = []

for i in range(len(lista) - 1,-1,-1): #Comece do último índice → vá até o índice 0 → andando para trás de 1 em 1.
    pegar_l = lista[i]
    lista_inv.append(pegar_l)
print(lista_inv)

#========= ex 5 =========#
nomes = ["Ana", "maria", "Alberto", "joao"]
contagem = 0

for x in nomes:
    x = x.lower()
    if (x [0] == "a"):
        contagem += 1
print(contagem)