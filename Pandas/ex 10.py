import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\DONIZETE\Downloads\dados_maquina_avancado.xlsx")

#========Exercicío 1=============#
linhas = df[
    (df["temperatura_c"] > 60) &
    (df["temperatura_c"] < 80) &
    (df["vibracao_mm_s"] < 6) &
    (df["pressao_bar"] > 10) &
    (df["pressao_bar"] < 15)
]
linhas = linhas.sort_values("temperatura_c")
linhas = linhas.reset_index(drop=True)

#print(linhas)

#===========Exercicío 2=============#
grupo = df.groupby(["status", "turno"])
contagem = grupo.size()
print("Contagem por grupo:\n", contagem)

filtro = contagem[contagem>2]
print("\nGrupos com mais de 2 máquinas:\n", filtro)

medias = grupo[["temperatura_c", "vibracao_mm_s", "pressao_bar"]].mean()
print("Médias por grupo:\n", medias)
