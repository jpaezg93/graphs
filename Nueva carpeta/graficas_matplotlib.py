# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% [markdown]
# Carga de datos:
# 
# Los datos obtenidos son de: ```<inserte link...>```

# %%
data = {
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4', 'Producto 5',
               'Producto 6', 'Producto 7', 'Producto 8', 'Producto 9', 'Producto 10',
               'Producto 11', 'Producto 12', 'Producto 13', 'Producto 14', 'Producto 15'],
    'Precio': [100, 150, 200, 120, 180, 250, 160, 140, 170, 190, 210, 230, 240, 220, 130],
    'Categoría': ['Electrónica', 'Electrónica', 'Ropa', 'Juguetes', 'Ropa',
                  'Ropa', 'Juguetes', 'Electrónica', 'Libros', 'Libros', 'Ropa',
                  'Electrónica', 'Ropa', 'Libros', 'Electrónica']
}

df = pd.DataFrame(data)

# %%
df

# %%
plt.style.use('fivethirtyeight')

# %%
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].boxplot(df["Precio"])
axs[0, 0].set_title("Distribución de Precios")
axs[0, 0].set_ylabel("Precio")

cat_counts = df["Categoría"].value_counts()
axs[0, 1].pie(cat_counts, labels=cat_counts.index, autopct="%1.1f%%")
axs[0, 1].set_title("Distribución de Categorías")

axs[1, 0].hist(
    df[df["Categoría"] == "Ropa"]["Precio"],
    bins=5,
    color="#00ffcc",
    alpha=0.7,
    edgecolor="black"
)
axs[1, 0].set_title("Histograma de precios (Ropa)")
axs[1, 0].set_xlabel("Precio")
axs[1, 0].set_ylabel("Frecuencia")

axs[1, 1].hist(
    df[df["Categoría"] == "Electrónica"]["Precio"],
    bins=5,
    edgecolor="black",
    color="#ff9999",
    alpha=0.7,
)
axs[1, 1].set_title("Histograma de precios (Electrónica)")
axs[1, 1].set_xlabel("Precio")
axs[1, 1].set_ylabel("Frecuencia")

plt.tight_layout()
# plt.show()
plt.savefig("reporte.pdf")


