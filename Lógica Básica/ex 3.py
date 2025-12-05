import math

class Vector:

    def __init__(self, *args):
        self.lista = list(args)
    
    def __str__(self):
        return (f"Vetor: {self.lista}")
    
    def __repr__(self):
        return (f"Vetor({self.lista})")
    
    def magnitude(self):
        quadrado = [x**2 for x in self.lista]
        soma = sum(quadrado)
        resultado = math.sqrt(soma)
        return resultado
    
    def __eq__(self, other):
        if isinstance (other, Vector):
            return self.lista == other.lista
        return NotImplemented
    
    def __lt__ (self, other):
       if isinstance (other, Vector):
            return self.magnitude() < other.magnitude()
       return NotImplemented
    
    def __add__ (self, other):
        novo_v = []
        if not isinstance(other, Vector):
            return NotImplemented
        
        if (len(self.lista) != len(other.lista)):
            return NotImplemented
        
        for x in range(len(self.lista)):
            novo_v.append(self.lista[x] + other.lista[x])

        return Vector(*novo_v)