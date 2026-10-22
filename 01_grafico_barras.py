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

df = pd.read_csv(DADOS / "dados_barras.csv")
tabela = df.pivot_table(index="categoria", columns="regiao", values="vendas_medias", aggfunc="mean")
ax = tabela.plot(kind="bar", figsize=(11, 6), width=0.8)
ax.set(title="Vendas médias por categoria e região", xlabel="Categoria", ylabel="Vendas médias")
ax.legend(title="Região")
ax.tick_params(axis="x", rotation=0)
ax.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "01_barras.png")
plt.close()
