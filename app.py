"""Dashboard TREXA · VICSON · SILLACA (Febeca) para Streamlit.

El dashboard completo vive en index.html; este app.py solo lo muestra dentro de Streamlit.
Local:  streamlit run app.py
Nube:   Streamlit Community Cloud -> repositorio de GitHub -> Main file path: app.py
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Reporte TREXA - VICSON",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Oculta el menú, encabezado y márgenes de Streamlit para que el dashboard use toda la pantalla.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner="Cargando dashboard…")
def cargar_html() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")


components.html(cargar_html(), height=1200, scrolling=True)
