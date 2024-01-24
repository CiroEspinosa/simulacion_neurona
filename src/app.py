import streamlit as st

st.title("Simulador de neurona")


num_x_w = st.slider("Elige el número de entradas/pesos que tendrá la neurona", min_value=1, max_value=10, value=3, key="s_pe")

# Crear columnas para los inputs de pesos
st.write("## Pesos")
pesos = []
for col in st.columns(num_x_w):
    with col:
        peso = st.number_input(f'w{len(peso)}', key=f'w{len(peso)}')
        pesos.append(peso)


st.write(f'w = {pesos}')

# Crear columnas para los inputs de entradas
st.write("## Entradas")
entradas = []
for i in range(num_x_w):
    entrada = st.number_input(f'x{i}', key=f'x{i}')
    entradas.append(entrada)

# Botón para calcular salida
btn_salida = st.button("Calcular salida", key="btn_salida")

if btn_salida:
    # Calcular la salida de la neurona
    y = sum(p * x for p, x in zip(pesos, entradas))
    st.write("La salida de la neurona es", y)

