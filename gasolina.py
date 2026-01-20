# código de geração do gráfico!

import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo gasolina.csv
df = pd.read_csv("gasolina.csv")

# Visualizar as primeiras linhas
df.head()

# Considerando:
# Primeira coluna → dia
# Segunda coluna → preço da gasolina

x_col = df.columns[0]
y_col = df.columns[1]

plt.figure()
plt.plot(df[x_col], df[y_col])
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title("Preço da Gasolina por Dia")
plt.tight_layout()

# Salvar o gráfico
plt.savefig("gasolina.png")

# Exibir o gráfico
plt.show()