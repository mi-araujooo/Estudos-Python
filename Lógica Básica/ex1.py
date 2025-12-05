import random
import math


class AnaliseNumerica:
    def __init__(self, limite):
        self.lista = list(range(1, limite +1, 1))

    def menor (self):
        return min(self.lista)
    
    def maior (self):
        return max(self.lista)
    
    def soma (self):
        return sum(self.lista)
    
    def media (self):
        return sum(self.lista) / len(self.lista)
    
    def mediana (self):
        lista_ord = sorted(self.lista)
        n = len(lista_ord)

        if(n%2 != 0):
            indice_mei = n // 2
            return lista_ord[indice_mei]
        else:
            indice_p = n //2 -1
            indice_s = n // 2
            return (lista_ord[indice_p] + lista_ord[indice_s])/ 2
        
    def moda(self):
        frequencias = {} #cria um dicionario para checar as frquencias

        for num in self.lista: #percorre cada númeor da lista
            if num not in frequencias: #"se o num não está na frequencia"
                frequencias[num] =1 #adiciona ele
            else:
                frequencias[num] +=1 #caso contrario adicona mais um no valor que j´´a tinha

        maior = max(frequencias.values()) #depois checa nas frequencias quem teve mais aparições (max)

        for num in frequencias: #agr ele vai verificar todos os numeros na frquencia
            if(frequencias[num]== maior): #se o dado numero da frquencia for o com mais aparições
                return num #retorna ele
    
    def variancia (self):
        soma = 0 #onde vai somar os valores da variabilidade
        m = self.media() #reaproveitado a função da media
        for num in self.lista: #percorre todos os numeros da lista
           soma += (num- m) ** 2 #a cada numero, eu pego ele, subrtrio pela media, e elevo a 2
           #no final coloco na variavel soma, juntando tds valores em um só
        
        variancia = soma / len(self.lista) #crio outra variavel que vai pegar a soma e vai dividir pelo tamanho total da lista
        return variancia

    def desv_padrao(self):
        v = self.variancia()
        desv = math.sqrt(v) #função que vem do math e tira raiz quadrada de qualq num
        return desv


    def relatorio(self):
        relatorio = {
            "média": self.media(),
            "mediana": self.mediana(),
            "moda": self.moda(),
            "variancia": self.variancia(),
            "desvio padrão" : self.desv_padrao(),
            "maior número" : self.maior(),
            "menor número" : self.menor()
        }
        return relatorio
    
    def normalizar(self):
        menor = self.menor()
        maior = self.maior()
        nova_list = []

        for num in self.lista:
            nova_list.append((num-menor)/(maior-menor))

        return nova_list
    
    def filtro (self):
        max_v = 10
        min_v = 1

        lista_filtrada = []
        for num in self.lista:
            if (min_v <=  num <= max_v):
                lista_filtrada.append(num)
        return lista_filtrada
    
    #def embaralhar (self):
        #random.shuffle(self.lista)
        #return self.lista
    


#==aba em que o user define o limite==#
lim = int(input("Digite um número: "))
obj = AnaliseNumerica(lim)
#=====================================#

print("Dados: ", obj.relatorio())
print("Lista normalizada: ", obj.normalizar())
print("Lista filtrada de 1 à 10: ", obj.filtro())