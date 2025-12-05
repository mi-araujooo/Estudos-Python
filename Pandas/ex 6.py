import pandas as pd 
df = pd.read_excel(r"C:\Users\DONIZETE\Downloads\dados_maquina.xlsx")
media_t = df["temperatura_c"].mean()
media_v = df["vibracao_mm_s"].mean()
media_p = df["pressao_bar"].mean()
alertas = df[df["temperatura_c"] > 70.00] #variavel de temperaturas maiores que 70

print(df.head(8))#primeiras linhaa
print(df.shape[0]) #qnt linhas
print(df.shape[1]) #qnt colunas
print({
    f"média temperatura: {media_t}",
    f"média vibração: {media_v}",
    f"média pressão: {media_p}"
}) #média de todas colunas
print(df["vibracao_mm_s"].max()) #maior valor
print(alertas) #temperaturas maiores que 70
print(df["status_vibracao"]) #temperaturas maiores que 70