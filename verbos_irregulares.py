import streamlit as st
import random

# Tus listas de datos
verbos = ["be","bear","beat","become","begin","bite","blow","break","bring","build","burn","burst","buy","can","catch","choose","come","cost","cut","deal","dig"]
Pasado = ["was","bore","beat","became","began", "bit","blew","broke","brought","built","burnt","burst","bought","could","caught","chose","came","cost","cut","dealt","dug"]
Traducción = ["ser","soportar","latir","convertirse","comenzar","morder","soplar","romper","traer algo","construir","quemar","explotar","comprar","poder","pillar","elegir","venir","costar","cortar","negociar","cavar"]

st.set_page_config(page_title="Práctica de Verbos", page_icon="📖")
st.title("🎯 Entrenador de Verbos Irregulares")

# Inicializamos el estado de la sesión para no perder el progreso
if 'indice' not in st.session_state:
    st.session_state.indice = random.randint(0, len(verbos)-1)
if 'errores' not in st.session_state:
    st.session_state.errores = 0

idx = st.session_state.indice

st.subheader(f"¿Cuál es el pasado simple de: **{verbos[idx]}**?")
st.info(f"Significado: {Traducción[idx]}")

# Entrada de texto del usuario
respuesta = st.text_input("Escribe tu respuesta aquí:", key="input_res").lower().strip()

if st.button("Comprobar"):
    if respuesta == Pasado[idx]:
        st.success(f"¡Correcto! {verbos[idx]} -> {Pasado[idx]}")
        # Cambiamos a un nuevo verbo
        st.session_state.indice = random.randint(0, len(verbos)-1)
        st.button("Siguiente Verbo")
    else:
        st.error("Incorrecto, ¡vuelve a intentarlo!")
        st.session_state.errores += 1

st.sidebar.write(f"Errores acumulados: {st.session_state.errores}")