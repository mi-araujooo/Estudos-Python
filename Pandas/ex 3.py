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

alertas = df[df["temperatura_c"] >= 70]
media_vibração = alert["vibracao_mm_s"].mean()

print(alertas)
print(media_vibração)