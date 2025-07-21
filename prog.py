import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Desintegración Radioactiva")

st.title("🧪 Simulación de Desintegración Radioactiva (Tiempo Fijo)")

# Entradas del usuario
N0 = st.number_input("Número inicial de núcleos (N₀)", min_value=1, value=1000)
halflife = st.number_input("Vida media (t½) en segundos", min_value=0.1, value=10.0)
tiempo_total = st.slider("Duración de la simulación (s)", min_value=10, max_value=120, value=60)
dt = st.slider("Intervalo de actualización (s)", min_value=0.1, max_value=2.0, value=0.5)

# Constante de desintegración
lambda_ = np.log(2) / halflife

# Contenedores de datos
datos_tiempo = []
datos_N = []

# Espacio para la gráfica
grafico = st.empty()

# Simulación en tiempo real
t = 0.0
while t <= tiempo_total:
    N = N0 * np.exp(-lambda_ * t)
    datos_tiempo.append(t)
    datos_N.append(N)

    # Crear gráfico con escala fija
    fig, ax = plt.subplots()
    ax.plot(datos_tiempo, datos_N, color='blue')
    ax.set_xlim(0, tiempo_total)
    ax.set_ylim(0, N0 * 1.05)
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Núcleos restantes")
    ax.set_title("Desintegración Radioactiva")

    grafico.pyplot(fig)

    t += dt
    time.sleep(dt)

st.success("✅ Simulación finalizada")

st.latex(r"N(t) = N_0 \cdot e^{-\lambda t}")
st.markdown(f"Donde λ = ln(2) / t½ = {lambda_:.4f} s⁻¹")
