# %%
import numpy as np

x = np.linspace(0, 10, 100)  # Valores x
y = np.sin(x)                # Valores y correspondientes

# %%
import plotly.graph_objects as go

# %% [markdown]
# ### Líneas

# %%
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="Gráfico de líneas",
    )
)

# %% [markdown]
# ### Dispersión

# %%
x_disp = np.random.rand(100)  # Valores x aleatorios
y_disp = np.random.rand(100)  # Valores y aleatorios

# %%
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x_disp,
        y=y_disp,
        mode="markers",
        name="Gráfico de dispersión",
    )
)

# %%
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x_disp,
        y=y_disp,
        mode="markers",
        marker={
            "size": 8,
            "color": "#ff99ff",
            "symbol": "diamond",
        },
        name="Gráfico de dispersión",
    )
)

# %% [markdown]
# ### Histogramas

# %%
x = ['A', 'B', 'C', 'D', 'E']  # Etiquetas de las barras
y = np.random.randint(1, 10, size=5)  # Alturas de las barras aleatorias

# %%
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=x,
        y=y,
        marker={
            "color": "red",
        },
        name="Gráfico de barras"
    )
)

# %% [markdown]
# ### Gráfico de torta

# %%
labels = ['A', 'B', 'C', 'D']  # Etiquetas de las categorías
values = [30, 20, 15, 35]  # Valores correspondientes a cada categoría

# %% [markdown]
# Documentación: https://plotly.com/python-api-reference/plotly.graph_objects.html

# %%
fig = go.Figure()

fig.add_trace(
    go.Pie(
        labels=labels,
        values=values,
        hole=0.5,
        marker={
            "colors": ["aliceblue", "antiquewhite", "aqua", "aquamarine"]
        },
        title="Gráfico de torta",
    )
)

fig.show()

# %% [markdown]
# ### Boxplot

# %%
np.random.seed(0)  # Establecer semilla para reproducibilidad
x = np.random.randn(100)  # Datos aleatorios para el gráfico de cajas

# %%
fig = go.Figure()

fig.add_trace(
    go.Box(
        y=x,
        name="Boxplot",
        boxpoints="all",
        whiskerwidth=0.3,
    )
)

fig.update_layout(
    template="plotly_dark"
)

fig.show()

# %% [markdown]
# ### Subplots

# %%
x = np.linspace(0, 2*np.pi, 100)  # Valores x comunes para ambos subplots
y1 = np.sin(x)  # Valores y para el primer subplot
y2 = np.cos(x)  # Valores y para el segundo subplot

# %%
import plotly.subplots as sp

# %%
fig = sp.make_subplots(2, 1)

fig.add_trace(
    go.Scatter(
        x=x,
        y=y1,
        mode="lines",
        name="Gráfica Seno",
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=y2,
        mode="lines",
        name="Gráfica Coseno",
    ),
    row=2,
    col=1,
)

fig.update_layout(
    title="Subplot trigonométrico",
    height=600,
    width=800,
)

fig.show()


