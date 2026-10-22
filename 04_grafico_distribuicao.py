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

df = pd.read_csv(DADOS / "dados_distribuicao.csv")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df["idade"], bins=12, color="#4682b4", edgecolor="white")
ax.set(title="Distribuição de idades dos clientes", xlabel="Idade (anos)", ylabel="Quantidade de clientes")
ax.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "04_distribuicao.png")
plt.close()
