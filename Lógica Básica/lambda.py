class Exemplos:
    #==soma *args==#
    def soma_valores(*args):
        total = 0
        for x in args:
            total += x
        return total
    
    #==informações *kwargs==#
    def mostra_info(**kwargs):
        for chave,valor in kwargs.item():
            print(f'{chave}: {valor}')

    #==lambda quadrado==#
    num = int(input("digite um número: "))
    quadrado = (lambda x: x**2)(num)
    print(quadrado)

    #==lambda triplo==#
    lista = [1,2,3,4,5,6,7,8,9,10]
    triplo = list(map(lambda x: x*3, lista))
    print(triplo)

    #==lambda filter==#
    pares = list(filter(lambda x: x%2==0, lista))
    print(pares)