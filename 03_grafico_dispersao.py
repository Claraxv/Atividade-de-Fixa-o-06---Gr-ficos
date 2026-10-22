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

df = pd.read_csv(DADOS / "dados_dispersao.csv")
fig, ax = plt.subplots(figsize=(10, 6))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo, alpha=0.72, s=43)
ax.set(title="Relação entre altura e peso", xlabel="Altura (cm)", ylabel="Peso (kg)")
ax.legend(title="Sexo")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(SAIDA / "03_dispersao.png")
plt.close()
