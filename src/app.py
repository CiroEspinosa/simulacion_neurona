import streamlit as st
from neurona import Neuron
import os

st.set_page_config(layout="wide")

ruta_imagen_local = os.path.join("img", "2480958_15286-removebg-preview.png")
st.image(ruta_imagen_local, width=200)
st.title("Simulador de neurona")

num_x_w = st.slider("Elige el número de entradas/pesos que tendrá la neurona", min_value=1, max_value=10, value=3, key="s_pe")

def_pesos = [0.5, 1.2, 6.8]
def_entradas = [4, 6, -3]
def_sesgo = 100
def_func = "relu"

def_pesos += [0] * max(0, num_x_w - len(def_pesos))
def_entradas += [0] * max(0, num_x_w - len(def_entradas))


pesos = []
st.write("### Pesos")
for col, def_peso in zip(st.columns(num_x_w), def_pesos):
    with col:
        peso = st.number_input(f'w$_{len(pesos)}$', key=f'w{len(pesos)}', value=float(def_peso))
        pesos.append(peso)

st.write(f'w = {pesos}')

entradas = []
st.write("### Entradas")
for col, def_entrada in zip(st.columns(num_x_w), def_entradas):
    with col:
        entrada = st.number_input(f'x$_{len(entradas)}$', key=f'x{len(entradas)}', value=float(def_entrada))
        entradas.append(entrada)

st.write(f'x = {entradas}')

col1, col2 = st.columns(2)
with col1:
    st.write("### Sesgo")
    sesgo = st.number_input("Introduce el valor del sesgo", value=float(def_sesgo))
with col2:
    st.write("### Función de activación")
    func_options = ["relu", "sigmoid", "tanh"]
    func = st.selectbox("Elige la función de activación", func_options, index=func_options.index(def_func))

btn_salida = st.button("Calcular salida", key="btn_salida")

if btn_salida:
    neurona = Neuron(weights=pesos, bias=sesgo, func=func)
    y = neurona.run(entradas)
    st.write("La salida de la neurona es", y)
