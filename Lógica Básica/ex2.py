class Exemplos:
    #==soma *args==#
    def soma_valores(self, *args):
        total = 0
        for x in args:
            total += x
        return total
    
    #==informações *kwargs==#
    def mostra_info(self, **kwargs):
        for chave,valor in kwargs.items():
            print(f'{chave}: {valor}')

    #==lambda quadrado==#
    def lamb_qad(x):
        return (lambda x: x**2)(x)

    #==lambda triplo==#
    lista = [1,2,3,4,5,6,7,8,9,10]
    triplo = list(map(lambda x: x*3, lista))
    print(triplo)

    #==lambda filter==#
    pares = list(filter(lambda x: x%2==0, lista))
    print(pares)

    #==lista quadrado==#
    quadrado = [x**2 for x in lista]
    print(quadrado)

    #==lista impares==#
    impares = [x for x in range(1,20+1,1) if x%2 != 0]
    print(impares)

num = int(input("digite um número: "))




class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return (f"Pessoa: {self.nome}, {self.idade} anos")
    
    def __repr__(self):
        return (f"Pessoa: nome={self.nome!r}, idade={self.idade!r}")
    
