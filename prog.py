import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tempfile
import os

st.set_page_config(page_title="Desintegración Radiactiva Animada")

st.title("📽️ Animación: Fracción Remanente vs. Número de Periodos")

# Parámetros del usuario
num_periodos = st.slider("Número total de periodos (t / t½)", min_value=1, max_value=20, value=10)
dt = st.slider("Paso entre puntos (fracción de vida media)", min_value=0.05, max_value=1.0, value=0.2)
guardar_video = st.checkbox("Guardar animación como video (.mp4)")

# Eje de tiempo normalizado
n_values = np.arange(0, num_periodos + dt, dt)
N_frac = np.exp(-np.log(2) * n_values)

# Crear la figura
fig, ax = plt.subplots()
ax.set_xlim(0, num_periodos)
ax.set_ylim(0, 1.05)
ax.set_xlabel("Número de periodos (t / t½)")
ax.set_ylabel("Fracción remanente (N / N₀)")
ax.set_title("Desintegración Radioactiva Normalizada")
ax.grid(True)

line, = ax.plot([], [], color='green', marker='o')

# Inicialización
def init():
    line.set_data([], [])
    return line,

# Animación
def update(frame):
    x = n_values[:frame]
    y = N_frac[:frame]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(
    fig, update, frames=len(n_values),
    init_func=init, blit=True, interval=300
)

# Mostrar la animación en Streamlit
from streamlit.components.v1 import html

with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
    ani.save(tmpfile.name, writer='html')
    with open(tmpfile.name, 'r') as f:
        html(f.read(), height=400)

# Guardar como video si se seleccionó
if guardar_video:
    with st.spinner("Generando video..."):
        video_path = os.path.join(tempfile.gettempdir(), "desintegracion.mp4")
        ani.save(video_path, writer='ffmpeg', fps=3)
        with open(video_path, "rb") as f:
            st.download_button("📥 Descargar video (.mp4)", f, file_name="desintegracion.mp4", mime="video/mp4")

# Mostrar fórmula
st.latex(r"\frac{N(t)}{N_0} = e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")
