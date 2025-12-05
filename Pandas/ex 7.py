import pandas as pd 
df = pd.read_excel(r"C:\Users\DONIZETE\Downloads\dados_maquina.xlsx")

df["status_vibracao"] = df["vibracao_mm_s"].apply(lambda x: "normal" if x < 5 else "alta" if x >=5 and x <=8 else "critica")
filtro = df[(df["temperatura_c"] > 60) & (df["vibracao_mm_s"]> 6)]
valores_f = filtro.sort_values("temperatura_c", ascending=False)

df["faixa_temp"] = df["temperatura_c"].apply(lambda x: "baixa" if x < 55 else "média" if 55 <= x <=70 else "alta")
calculo = df["faixa_temp"].value_counts()


filtro_v =  df[df["vibracao_mm_s"]> 7]
med_v = filtro_v["vibracao_mm_s"].mean()
min_v = filtro_v["vibracao_mm_s"].min()
max_v = filtro_v["vibracao_mm_s"].max()
desv_p = filtro_v["vibracao_mm_s"].std()


novo_df = df[["temperatura_c", "vibracao_mm_s"]]
novo_df.to_csv('subset_maquina.csv', index=False)

print(valores_f)
print(calculo)