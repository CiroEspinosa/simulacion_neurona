import streamlit as st
from neurona import Neuron

st.title("Simulador de neurona")

num_x_w = st.slider("Elige el número de entradas/pesos que tendrá la neurona", min_value=1, max_value=10, value=3, key="s_pe")

# Valores por defecto para el caso n1 = Neuron(weights=[0.5, 1.2, 6.8], bias=100, func="relu")
default_pesos = [0.5, 1.2, 6.8]
default_entradas = [4, 6, -3]
default_sesgo = 100
default_func = "relu"

# Widgets para que el usuario pueda modificar los valores por defecto
pesos = []
for col, default_peso in zip(st.columns(num_x_w), default_pesos):
    with col:
        peso = st.number_input(f'w$b_{len(pesos)}$', key=f'w{len(pesos)}', value=default_peso)
        pesos.append(peso)

st.write(f'w = {pesos}')

entradas = []
for col, default_entrada in zip(st.columns(num_x_w), default_entradas):
    with col:
        entrada = st.number_input(f'x<sub>{len(entradas)}</sub>', key=f'x{len(entradas)}', value=default_entrada)
        entradas.append(entrada)

st.write(f'x = {entradas}')

col1, col2 = st.columns(2)
with col1:
    st.write("### Sesgo")
    sesgo = st.number_input("Introduce el valor del sesgo", value=default_sesgo)
with col2:
    st.write("### Función de activación")
    func_options = ["relu", "sigmoid", "tanh"]
    func = st.selectbox("Elige la función de activación", func_options, index=func_options.index(default_func))

btn_salida = st.button("Calcular salida", key="btn_salida")

if btn_salida:
    neurona = Neuron(weights=pesos, bias=sesgo, func=func)
    y = neurona.run(entradas)
    st.write("La salida de la neurona es", y)
