import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración de la página
st.set_page_config(page_title="Desintegración Radiactiva - Fracción vs Periodos")

st.title("📉 Desintegración Radiactiva: Fracción remanente vs Número de Periodos")

# Entradas del usuario
num_periodos = 10 
dt = 1
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
    N_frac = 1 - np.exp(-lambda_ln2 * n)  # N(t)/N0 = 1- e^(-ln(2) * n)
    datos_n.append(n)
    datos_frac.append(N_frac)

    # Graficar con escala fija
    fig, ax = plt.subplots()
    ax.plot(datos_n, datos_frac, color='green', marker='o', linestyle='-')
    ax.set_xlim(0, num_periodos)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Número de periodos ")
    ax.set_ylabel("Fracción de actividad de saturación o desintegración")
    #ax.set_title("Desintegración Radioactiva Normalizada")
    ax.grid(True)
    grafico.pyplot(fig)

    n += dt
    time.sleep(1)

# Mostrar fórmula final
st.latex(r"1-e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")
st.markdown("Donde:")
st.markdown("- \( N_0 \) es el número inicial de núcleos")
st.markdown("- \( t_{1/2} \) es la vida media")
st.markdown("- \( n = t / t_{1/2} \) es el número de periodos")

st.success("✅ Simulación completada.")
