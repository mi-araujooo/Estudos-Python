import pandas as pd

# Dados falsos de sensores de uma máquina
dados = {
    "tempo_s": list(range(1, 11)),   # 1 até 10
    "temperatura_c": [60, 62, 63, 65, 67, 70, 72, 75, 77, 80],
    "vibracao_mm_s": [2.1, 2.2, 2.4, 2.3, 2.6, 2.8, 3.1, 3.0, 3.3, 3.5],
    "status": [
        "normal", "normal", "normal", "normal", "normal",
        "alerta", "alerta", "alerta", "alerta", "critico"
    ]
}


df = pd.DataFrame(dados)

decres = df.sort_values("vibracao_mm_s", ascending=False)
df["risco"] = df["temperatura_c"].apply(lambda x: "alto" if x > 75 else "baixo")
alert = df[df["status"] == "alerta"]



print(decres)
print(df)
print(alert)
