import pandas as pd

dados = {
    "nome": ["Ana", "João", "Milene"],
    "idade": [20, 25, 22],
    "nota": [8.5, 7.0, 9.2]
} #dicionario que contém as informações

df = pd.DataFrame(dados) #variavel que cria um Dataframe a partir do dicionario dados
print(df["idade"] > 21)