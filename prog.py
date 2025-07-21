import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

st.set_page_config(page_title="Acumulación de Actividad - Dos Núclidos")

st.title("☢️ Acumulación de Actividad de Dos Radionúclidos")

# Parámetros del usuario
st.sidebar.header("Radionúclido A")
t12_a = st.sidebar.number_input("Valor t½ de A [s]", min_value=0.01, value=5.0)
nombre_a = st.sidebar.text_input("Nombre A", value="Elemento A")

st.sidebar.header("Radionúclido B")
t12_b = st.sidebar.number_input("Valor t½ de B [s]", min_value=0.01, value=10.0)
nombre_b = st.sidebar.text_input("Nombre B", value="Elemento B")

num_periodos = st.slider("Número total de periodos (referencia)", 1, 20, 10)
dt = st.slider("Paso entre puntos (s)", 0.1, 5.0, 1.0)

# Calcular número de pasos y tiempo total basado en el mayor t½
t_ref = max(t12_a, t12_b)
t_total = num_periodos * t_ref
t_values = np.arange(0, t_total + dt, dt)

# Constante de desintegración para cada uno
lambda_a = np.log(2) / t12_a
lambda_b = np.log(2) / t12_b

# Fracción acumulada: 1 - exp(-lambda * t)
frac_a = 1 - np.exp(-lambda_a * t_values)
frac_b = 1 - np.exp(-lambda_b * t_values)
n_periodos = t_values / t_ref

# Gráfica
fig, ax = plt.subplots()
ax.plot(n_periodos, frac_a, label=f"{nombre_a} (t½ = {t12_a}s)", color='blue', marker='o')
ax.plot(n_periodos, frac_b, label=f"{nombre_b} (t½ = {t12_b}s)", color='red', marker='s')
ax.axhline(1.0, color='gray', linestyle='--', linewidth=1)
ax.set_xlim(0, num_periodos)
ax.set_ylim(0, 1.05)
ax.set_xlabel("Número de periodos normalizados (t / t½ de referencia)")
ax.set_ylabel("Fracción acumulada (N / N₀)")
ax.set_title("Acumulación de Actividad de Dos Radionúclidos")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Tabla de datos
tabla = pd.DataFrame({
    "t (s)": t_values,
    "n (t / t_ref)": n_periodos,
    f"{nombre_a} (N/N₀)": frac_a,
    f"{nombre_b} (N/N₀)": frac_b,
})
st.dataframe(tabla)

# Ecuación general
st.latex(r"\frac{N(t)}{N_0} = 1 - e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")
st.markdown("Se muestran dos curvas de acumulación para diferentes vidas medias. El eje horizontal está normalizado respecto a la mayor de ambas vidas medias.")

st.success("✅ Simulación completada.")
