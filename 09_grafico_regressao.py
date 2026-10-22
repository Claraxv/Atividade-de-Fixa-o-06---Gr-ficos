from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DADOS = BASE / "dados"
SAIDA = BASE / "graficos"
SAIDA.mkdir(exist_ok=True)
plt.rcParams.update({"figure.dpi": 120, "savefig.dpi": 160, "font.size": 11})

import numpy as np

df = pd.read_csv(DADOS / "dados_regressao.csv")
x = df["renda_mensal"].to_numpy()
y = df["gasto_mensal"].to_numpy()
inclinacao, intercepto = np.polyfit(x, y, 1)
x_reta = np.linspace(x.min(), x.max(), 200)
y_previsto = inclinacao * x + intercepto
r2 = 1 - np.sum((y - y_previsto) ** 2) / np.sum((y - y.mean()) ** 2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x, y, alpha=0.65, label="Observações")
ax.plot(x_reta, inclinacao * x_reta + intercepto, color="#d04b3e", linewidth=2, label=f"Regressão linear (R² = {r2:.3f})")
ax.set(title="Regressão linear: renda mensal x gasto mensal", xlabel="Renda mensal (R$)", ylabel="Gasto mensal (R$)")
ax.legend()
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "09_regressao.png")
plt.close()
print(f"Equação: gasto = {inclinacao:.4f} × renda + {intercepto:.2f}; R² = {r2:.4f}")
