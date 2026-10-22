# Atividade de Python — Visualização de Dados

Projeto com **9 gráficos**, cada um gerado por **um script Python independente** a partir dos arquivos CSV fornecidos.

## Como executar

1. Instale Python 3.10 ou superior.
2. Abra o terminal na pasta do projeto e instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Execute individualmente cada script, por exemplo:

   ```bash
   python 01_grafico_barras.py
   python 02_grafico_boxplot.py
   python 03_grafico_dispersao.py
   python 04_grafico_distribuicao.py
   python 05_grafico_frequencia.py
   python 06_grafico_heatmap.py
   python 07_grafico_linhas.py
   python 08_grafico_pizza.py
   python 09_grafico_regressao.py
   ```

Os arquivos PNG são salvos automaticamente na pasta `graficos/`. Os CSVs originais estão em `dados/`. Os scripts encontram suas pastas independentemente do diretório de onde forem executados.

## Gráficos

| Script | Arquivo de dados | Gráfico |
| --- | --- | --- |
| `01_grafico_barras.py` | `dados_barras.csv` | Barras agrupadas: vendas médias por categoria e região |
| `02_grafico_boxplot.py` | `dados_boxplot.csv` | Boxplot: salários por departamento |
| `03_grafico_dispersao.py` | `dados_dispersao.csv` | Dispersão: altura versus peso, por sexo |
| `04_grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma: idades dos clientes |
| `05_grafico_frequencia.py` | `dados_frequencia.csv` | Barras de frequência: tipos de atendimento |
| `06_grafico_heatmap.py` | `dados_heatmap.csv` | Heatmap: movimento por dia e horário |
| `07_grafico_linhas.py` | `dados_linhas.csv` | Linhas: evolução das vendas por loja |
| `08_grafico_pizza.py` | `dados_pizza.csv` | Pizza: participação no faturamento por canal |
| `09_grafico_regressao.py` | `dados_regressao.csv` | Dispersão e regressão linear: renda versus gasto, com R² |

## Publicação no GitHub

Crie um repositório no GitHub, por exemplo `atividade-graficos-python`, e envie **todo o conteúdo desta pasta**. Se preferir o terminal, rode na pasta do projeto:

```bash
git init
git add .
git commit -m "Adiciona scripts e graficos da atividade"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/atividade-graficos-python.git
git push -u origin main
```

Substitua `SEU_USUARIO` pelo seu usuário no GitHub e crie previamente o repositório vazio no site.

**Entrega:** envie ao professor o link do repositório público no GitHub.
