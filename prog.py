import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración de la página
st.set_page_config(page_title="Desintegración Radiactiva - Fracción vs Periodos")

st.title("📉 Desintegración Radiactiva: Fracción remanente vs Número de Periodos")

# Entradas del usuario
num_periodos = st.slider("Número total de periodos (t / t½)", min_value=1, max_value=20, value=10)
dt = st.slider("Paso entre puntos (fracción de vida media)", min_value=0.05, max_value=1.0, value=0.2)

# Parámetro constante
lambda_ln2 = np.log(2)  # ln(2)

# Inicializar listas para graficar
datos_n = []
datos_frac = []

# Contenedor para la gráfica
grafico = st.empty()

# Simulación
n = 0.0
while n <= num_periodos:
    N_frac = np.exp(-lambda_ln2 * n)  # N(t)/N0 = e^(-ln(2) * n)
    datos_n.append(n)
    datos_frac.append(N_frac)

    # Graficar con escala fija
    fig, ax = plt.subplots()
    ax.plot(datos_n, datos_frac, color='green', marker='o', linestyle='-')
    ax.set_xlim(0, num_periodos)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Número de periodos (t / t½)")
    ax.set_ylabel("Fracción remanente (N / N₀)")
    ax.set_title("Desintegración Radioactiva Normalizada")

    grafico.pyplot(fig)

    n += dt
    time.sleep(0.3)

# Mostrar fórmula final
st.latex(r"\frac{N(t)}{N_0} = e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")
st.markdown("Donde:")
st.markdown("- \( N_0 \) es el número inicial de núcleos")
st.markdown("- \( t_{1/2} \) es la vida media")
st.markdown("- \( n = t / t_{1/2} \) es el número de periodos")

st.success("✅ Simulación completada.")
