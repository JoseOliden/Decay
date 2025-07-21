import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Título de la app
st.title("Animación de la Desintegración Radiactiva")

# Parámetros de entrada
N0 = st.number_input("Número inicial de núcleos (N₀)", min_value=1, value=1000)
halflife = st.number_input("Vida media (t½) en segundos", min_value=0.1, value=10.0)
t_max = st.number_input("Tiempo total de simulación (s)", min_value=1, value=60)

# Cálculo de lambda
lambda_ = np.log(2) / halflife
t = np.linspace(0, t_max, 300)
N = N0 * np.exp(-lambda_ * t)

# Gráfico base
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, t_max)
ax.set_ylim(0, N0)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Núcleos restantes")
ax.set_title("Desintegración Radiactiva")

# Funciones para la animación
def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = t[:i]
    y = N[:i]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(t), interval=50, blit=True)

# Mostrar la animación en Streamlit
from streamlit.components.v1 import html
import tempfile

with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
    ani.save(f.name, writer='html')
    with open(f.name, 'r') as f_html:
        html(f_html.read(), height=400)

st.markdown("La ecuación usada es:  \n"
            r"$N(t) = N_0 \cdot e^{-\lambda t}$  \n"
            f"donde:  \n"
            r"$\lambda = \frac{{\ln(2)}}{{t_{1/2}}} = {lambda_:.4f} \ s^{{-1}}$")
