import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("usuarios.csv")

sexo_masculino = df[df["sexo"] == "M"] 

# print(sexo_masculino)

df["categoria"] = df["sexo"].apply(lambda sexo: "TI" if sexo == "M" else "RH" )

df.to_csv("usuarioSave.csv", index = False)

dfNew = pd.read_csv("usuarioSave.csv")

print(dfNew)

dfNew["categoria"].value_counts().plot(kind="bar")
plt.title("Categoria por Sexo")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")

plt.show()