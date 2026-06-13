# 📑 PROMPT DE CONTEXTO: ESTADO DEL PROYECTO CASHBACK

## 📝 Resumen del Proyecto y Contexto Actual
Este es un proyecto modular de Análisis de Datos enfocado en el modelo de negocio del **Cashback**. El repositorio está configurado en un Mac utilizando Visual Studio Code, Git y GitHub. El entorno virtual de Python (`.venv`) está instalado de forma aislada y limpia dentro de la subcarpeta raíz del repositorio de GitHub (`mi-proyecto-modular1`). 

### ✅ Lo que ya está hecho y configurado:
1. **Conexión Git/GitHub:** El repositorio local está perfectamente vinculado al remoto.
2. **Estructura de Carpetas Profesional:** Creada según los requisitos de la tutoría (`data/raw`, `data/processed`, `notebooks`, `reports/figures`, `src/`).
3. **Entorno Virtual (`.venv`):** Operativo en Mac, sincronizado como intérprete en VS Code y con las librerías base instaladas (`pandas`, `matplotlib`, `seaborn`, `notebook`, `faker`).
4. **Archivos Base:** Creados los archivos estructurales (`.gitignore` configurado para omitir el `.venv`, `requirements.txt`, `README.md` detallado con las 7 preguntas de negocio, `main.py`, y los scripts vacíos en `src/`).
5. **Script de Datos Sintéticos:** Se creó y probó con éxito un script funcional (`generar_dataset.py`) para generar datos con la suciedad requerida por la escuela (comas decimales, nulos, países inconsistentes), aunque se ha pausado para priorizar un enfoque con datos reales.

---

## 🛑 ¿Dónde nos hemos quedado?
Nos hemos quedado justo en el punto de inicio de la fase de **Adquisición de Datos**. Hemos validado las reglas del archivo `robots.txt` de la red de afiliación Awin (comprobando que permite el raspado) y hemos definido una **estrategia mixta de datos reales** para asegurar la máxima calidad técnica sin penalizar el tiempo de entrega.

---

## 🚀 Próximos pasos a seguir en la siguiente sesión:
Cuando retome este proyecto, el objetivo será ejecutar las siguientes tareas en orden:

1. **Estrategia Mixta de Datos Reales:**
   * **Paso A (Scraping):** Crear un mini-script de Web Scraping en `src/` (usando `requests` y `BeautifulSoup`) para extraer de forma verídica unas 30-40 marcas y sus ofertas actuales directamente de la web de una plataforma como iGraal o Letyshops.
   * **Paso B (Volumen Transaccional):** Buscar y descargar un dataset real de comercio electrónico o comportamiento de compra de más de 1,000 filas en **Kaggle** o **Hugging Face** (ej: *Customer Shopping Trends Dataset*), y guardarlo en `data/raw/`.
2. **Fusión y Ensuciamiento:** En el pipeline, cruzar la tabla grande con las marcas del scraping e introducir controladamente las imperfecciones técnicas exigidas por la tutoría.
3. **Fase de Análisis Exploratorio:** Abrir el Jupyter Notebook `notebooks/eda_analisis.ipynb` para empezar a inspeccionar la tabla con Pandas y responder las 7 preguntas mediante gráficos con intención (incluyendo el Heatmap).
