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

df = pd.read_csv(DADOS / "dados_pizza.csv")
fig, ax = plt.subplots(figsize=(9, 7))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%", startangle=90, pctdistance=0.75)
ax.set_title("Participação dos canais no faturamento")
ax.axis("equal")
plt.tight_layout()
plt.savefig(SAIDA / "08_pizza.png")
plt.close()
