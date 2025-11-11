import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Programes funcions elementals 💻")
st.write("Calculadora del vèrtex d'una paràbola")

# Entradas del usuario
a = st.number_input("Valor de a:", value=1.0)
b = st.number_input("Valor de b:", value=0.0)
c = st.number_input("Valor de c:", value=0.0)

# Botón para calcular
if st.button("Calcular i Graficar"):
    if a == 0:
        st.error("❌ El valor de 'a' no pot ser 0 (no seria una paràbola).")
    else:
        # Cálculo del vértice
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        st.success(f"Vèrtex: ({x:.2f}, {y:.2f})")

        # Crear gráfica
        domini = np.linspace(x - 50, x + 50, 400)
        recorregut = a * domini**2 + b * domini + c

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(domini, recorregut, label="Paràbola", color='#FF81C0')
        ax.plot(x, y, 'o', color='turquoise', label="Vèrtex")
        ax.set_title("Gràfica de la funció quadràtica", color='#FF81C0')
        ax.set_xlabel("x", color='pink')
        ax.set_ylabel("y", color='pink')
        ax.grid(True)
        ax.legend()
        ax.axhline(0, color='pink', linewidth=1)
        ax.axvline(0, color='pink', linewidth=1)

        st.pyplot(fig)
