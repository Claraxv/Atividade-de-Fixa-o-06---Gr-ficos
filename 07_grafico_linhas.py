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

df = pd.read_csv(DADOS / "dados_linhas.csv", parse_dates=["data"])
fig, ax = plt.subplots(figsize=(11, 6))
for loja, grupo in df.sort_values("data").groupby("loja"):
    ax.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3, linewidth=1.6, label=loja)
ax.set(title="Evolução das vendas por loja", xlabel="Data", ylabel="Vendas")
ax.legend(title="Loja")
ax.grid(alpha=0.2)
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig(SAIDA / "07_linhas.png")
plt.close()
