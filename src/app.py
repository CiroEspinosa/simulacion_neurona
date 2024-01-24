import streamlit as st
import os



ruta_imagen_local = os.path.join("img", "2480958_15286-removebg-preview.png")
st.image(ruta_imagen_local)

st.title("¡Hola neurona!")


tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=2.5, key="w0_t3")
        x0 = st.number_input("Entrada x₀", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x0_t3")
    with col2:
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=2.5, key="w1_t3")
        x1 = st.number_input("Entrada x₁", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x1_t3")
    with col3:
        w2 = st.slider("Peso w₂", min_value=0.0, max_value=5.0, value=2.5, key="w2_t3")
        x2 = st.number_input("Entrada x₂", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x2_t3")
    b = st.number_input("Introduzca el sesgo", key="b_t3")
    boton_calcular_salida_t3 = st.button("Calcular salida", key="boton_t3")

    if boton_calcular_salida_t3:
        y = x0 * w0 + x1 * w1 + x2 * w2 + b
        st.write("Salida:", y)

with tab2:

    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=2.5, key="w0_t2")
        x0 = st.number_input("Entrada x₀", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x0_t2")
    with col2:
        w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=2.5, key="w1_t2")
        x1 = st.number_input("Entrada x₁", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x1_t2")

    boton_calcular_salida_t2 = st.button("Calcular salida", key="boton_t2")

    if boton_calcular_salida_t2:
        y = x0 * w0 + x1 * w1
        st.write("Salida:", y)

with tab1:
    w = st.slider("Peso w", min_value=0.0, max_value=5.0, value=2.5, key="w_t1")
    x = st.number_input("Entrada x", min_value=2.0, max_value=3.0, value=2.5, format="%f", key="x_t1")
    boton_calcular_salida_t1 = st.button("Calcular salida", key="boton_t1")

    if boton_calcular_salida_t1:
        y = x * w
        st.write("Salida:", y)
