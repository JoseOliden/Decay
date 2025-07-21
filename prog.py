import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Desintegración Radioactiva en Tiempo Real")

st.title("📉 Desintegración Radioactiva en Tiempo Real")

# Entradas del usuario
N0 = st.number_input("Número inicial de núcleos (N₀)", min_value=1, value=1000)
halflife = st.number_input("Vida media (t½) en segundos", min_value=0.1, value=10.0)
tiempo_total = st.slider("Duración de la simulación (s)", min_value=5, max_value=60, value=30)
update_interval = st.slider("Intervalo de actualización (s)", min_value=0.1, max_value=1.0, value=0.2)

# Constante de desintegración
lambda_ = np.log(2) / halflife

# Gráfico dinámico
st.subheader("Evolución temporal de N(t)")
grafico = st.line_chart()

# Simulación en tiempo real
t = 0
datos_tiempo = []
datos_N = []

with st.empty():
    while t <= tiempo_total:
        N = N0 * np.exp(-lambda_ * t)
        datos_tiempo.append(t)
        datos_N.append(N)
        grafico.add_rows({"Núcleos": [N]})
        t += update_interval
        time.sleep(update_interval)

st.success("✅ Simulación terminada")

st.latex(r"N(t) = N_0 \cdot e^{-\lambda t}")
st.markdown(f"Donde:  \n- λ = ln(2) / t½ = {lambda_:.4f} s⁻¹")

