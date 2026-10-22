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

df = pd.read_csv(DADOS / "dados_heatmap.csv")
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
horarios = sorted(df["horario"].unique())
tabela = df.pivot_table(index="dia_semana", columns="horario", values="movimento_clientes", aggfunc="mean").reindex(index=dias, columns=horarios)
fig, ax = plt.subplots(figsize=(11, 6))
im = ax.imshow(tabela.values, cmap="YlOrRd", aspect="auto")
ax.set_xticks(range(len(horarios)), horarios)
ax.set_yticks(range(len(dias)), dias)
for i in range(len(dias)):
    for j in range(len(horarios)):
        valor = tabela.iloc[i, j]
        if pd.notna(valor): ax.text(j, i, f"{valor:.0f}", ha="center", va="center", fontsize=9)
fig.colorbar(im, ax=ax, label="Movimento de clientes")
ax.set(title="Movimento de clientes por dia e horário", xlabel="Horário", ylabel="Dia da semana")
plt.tight_layout()
plt.savefig(SAIDA / "06_heatmap.png")
plt.close()
