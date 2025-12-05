import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\DONIZETE\Downloads\dados_maquina.xlsx")


#=======gráfico histograma=========#
plt.hist(df["temperatura_c"], bins='auto', color='skyblue', edgecolor='black')
plt.title("Distribuição da Temperatura")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Frequência")
plt.show()


#=======gráfico de médias=========#
medias = df[["temperatura_c", "vibracao_mm_s", "pressao_bar"]].mean()
medias.plot(kind= 'bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title("Média de cada variável")
plt.ylabel("Valor médio")
plt.show()

#=======gráfico por group by (temperatura)=========#
df["faixa_temperatura"] = df["temperatura_c"].apply(lambda x: "baixa" if x < 65 else "média" if 65<x<70 else "alta")
contagem_faixa_t = df.groupby("faixa_temperatura").size()
contagem_faixa_t.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'], edgecolor='black')
plt.title("Distribuição de Temperatura por Faixa")
plt.xlabel("Faixa de Temperatura")
plt.ylabel("Quantidade de Valores")
plt.show()

#=======gráfico por group by (vibração)=========#
df["faixa_vibração"] = df["vibracao_mm_s"].apply(lambda x: "baixa" if x < 5 else "média" if 5<x<7 else "alta")
contagem_faixa_v = df.groupby("faixa_vibração").size()
contagem_faixa_v.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'], edgecolor='black')
plt.title("Distribuição de Vibração por Faixa")
plt.xlabel("Faixa de Vibração")
plt.ylabel("Quantidade de Valores")
plt.show()

#=======gráfico por group by (pressão)=========#
df["faixa_pressão"] = df["pressao_bar"].apply(lambda x: "baixa" if x < 10 else "média" if 10<x<15 else "alta")
contagem_faixa_p = df.groupby("faixa_pressão").size()
contagem_faixa_p.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'], edgecolor='black')
plt.title("Distribuição de Presão por Faixa")
plt.xlabel("Faixa de Presão")
plt.ylabel("Quantidade de Valores")
plt.show()


#=======juntando os três=========#
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 linha, 3 colunas
# Temperatura
contagem_faixa_t.reindex(["baixa", "média", "alta"]).plot(
    kind='bar', color='skyblue', edgecolor='black', ax=axes[0], title="Temperatura"
)
# Vibração
contagem_faixa_v.reindex(["baixa", "média", "alta"]).plot(
    kind='bar', color='salmon', edgecolor='black', ax=axes[1], title="Vibração"
)
# Pressão
contagem_faixa_p.reindex(["baixa", "média", "alta"]).plot(
    kind='bar', color='lightgreen', edgecolor='black', ax=axes[2], title="Pressão"
)
plt.tight_layout()
plt.show()