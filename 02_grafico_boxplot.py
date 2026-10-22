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

df = pd.read_csv(DADOS / "dados_boxplot.csv")
grupos = [grupo["salario"].values for _, grupo in df.groupby("departamento", sort=True)]
nomes = sorted(df["departamento"].unique())
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(grupos, tick_labels=nomes, patch_artist=True, boxprops={"facecolor": "#9dc7e8"}, medianprops={"color": "#aa3e32", "linewidth": 2})
ax.set(title="Distribuição de salários por departamento", xlabel="Departamento", ylabel="Salário (R$)")
ax.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "02_boxplot.png")
plt.close()
