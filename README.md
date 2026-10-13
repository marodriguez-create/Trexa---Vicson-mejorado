# Dashboard TREXA · VICSON · SILLACA (Febeca)

Reporte de ventas en toneladas (TREXA, VICSON y SILLACA). El dashboard es el archivo `index.html`
y `app.py` lo muestra dentro de Streamlit.

## Archivos
- `app.py` — aplicación de Streamlit (archivo principal).
- `index.html` — el dashboard completo.
- `requirements.txt` — dependencias (`streamlit`).
- `.streamlit/config.toml` — configuración (permite cargar el archivo grande).

## Subir a GitHub
1. Crea un repositorio nuevo en GitHub (por ejemplo `dashboard-trexa-vicson`).
2. Sube todo el contenido de esta carpeta (incluida la carpeta oculta `.streamlit`).

## Enlazar con Streamlit
1. Entra a https://share.streamlit.io e inicia sesión con GitHub.
2. **Create app** → elige el repositorio y la rama `main`.
3. **Main file path:** `app.py` → **Deploy**.

Para probar en tu PC: `pip install -r requirements.txt` y `streamlit run app.py`.

## Cómo se usa
- Sin clave, el dashboard es de **solo lectura**: se ven todas las pestañas, sin editar.
- Con la clave en "Clave para editar" se activa el modo editor (cargar reporte del día, habilitar nuevo mes, SILLACA, celdas editables).
- Clave inicial: `Febeca2026`. Cámbiala con "Cambiar clave" en modo editor.

## Importante
- Lo que actualizas en el navegador (reporte del día, mes habilitado, SILLACA) se guarda **solo en ese navegador**.
  Para que otras personas vean la actualización, reemplaza `index.html` en GitHub por el archivo actualizado y Streamlit se redespliega solo.
- La clave va dentro del archivo: evita ediciones accidentales, no es seguridad fuerte.
- El repositorio contiene los datos de ventas: usa un repositorio **privado** si no deben ser públicos (Streamlit Community Cloud acepta repos privados).
