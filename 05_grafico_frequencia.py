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

df = pd.read_csv(DADOS / "dados_frequencia.csv")
contagem = df["tipo_atendimento"].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(contagem.index, contagem.values, color="#579c87")
ax.bar_label(barras, padding=3)
ax.set(title="Frequência por tipo de atendimento", xlabel="Tipo de atendimento", ylabel="Quantidade de chamados")
ax.set_ylim(0, contagem.max() * 1.15)
ax.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "05_frequencia.png")
plt.close()
