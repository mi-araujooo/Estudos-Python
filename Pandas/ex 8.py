import pandas as pd 
df = pd.read_excel(r"C:\Users\DONIZETE\Downloads\dados_maquina.xlsx")

df["risco_operacional"] = df.apply(lambda row:
    "ALTO" if (row["temperatura_c"] > 70 and row["vibracao_mm_s"] > 7) 
    else "MÉDIO" if (60 < row["temperatura_c"] < 70 and 5 < row["vibracao_mm_s"] <7)
    else "BAIXO",
    axis=1
    )

df["faixa_pressao"] = df["pressao_bar"].apply(lambda x: "baixa" if x < 10 else "média" if 10<x<15 else "alta")
grupo = df.groupby("faixa_pressao")
#print(grupo["temperatura_c"].mean())
#print(grupo["vibracao_mm_s"].mean())
grupo["temperatura_c"].std()
grupo["vibracao_mm_s"].max()
grupo.size() 


df["score_saude"] = (
    df["temperatura_c"] * 0.4 +
    df["vibracao_mm_s"] * 0.3 +
    df["pressao_bar"] * 0.3
)
maiores = df["score_saude"].nlargest(5)
menores = df["score_saude"].nsmallest(5)
novo_df = pd.DataFrame({
    "maiores": maiores.values,
    "menores": menores.values
})
novo_df.to_csv('novos_val.csv', index=False)


linhas = df[
    (df["temperatura_c"]> 65) & 
    (df["temperatura_c"]< 80) & 
    (df["vibracao_mm_s"] < 6) & 
    (df["pressao_bar"] > 10)
]
linhas = linhas.sort_values("temperatura_c")
linhas = linhas.reset_index(drop=True)

temp_maior_70 = df[df["temperatura_c"] > 70]
vibr_maior_8 = df[df["vibracao_mm_s"] > 8]
pressao_12_16 = df[(df["pressao_bar"] > 12) & (df["pressao_bar"] < 16)]

relatorio= {
    "maior temperatura": float(df["temperatura_c"].max()),
    "menor temperatura": float(df["temperatura_c"].min()),
    "média da temperatura": float(df["temperatura_c"].mean()),
    "maior vibração": float(df["vibracao_mm_s"].max()),
    "menor vibração": float(df["vibracao_mm_s"].min()),
    "média vibração": float(df["vibracao_mm_s"].mean()),
    "maior pressão": float(df["pressao_bar"].max()),
    "menor pressão": float(df["pressao_bar"].min()),
    "média pressão": float(df["pressao_bar"].mean()),
    "quantidade de linhas acima de 70°C" : temp_maior_70.shape[0],
    "quantidade de linhas com vibração > 8" : vibr_maior_8.shape[0],
    "quantidade de linhas com pressão entre 12 e 16": pressao_12_16.shape[0]
}

print(relatorio)