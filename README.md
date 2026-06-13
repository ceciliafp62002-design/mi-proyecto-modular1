# 💰 Estudio de Mercado y Pipeline de Datos: Ecosistema Cashback

## 📋 Objetivo del Proyecto
Este proyecto realiza un análisis integral del modelo de negocio de **Cashback** (Fintech/Marketing de Afiliación) en España y Europa. El objetivo es evaluar el comportamiento del consumidor, comparar las ofertas de las principales aplicaciones del mercado (ej. iGraal, Letyshops, Awin) y detectar oportunidades de negocio mediante un pipeline de datos reproducible, limpio y modular.

---

## 🔍 Preguntas de Investigación
El análisis y las visualizaciones de este repositorio responden a las siguientes preguntas clave:
1. **Sectores dominantes:** ¿Qué categorías de tiendas (Moda, Viajes, Tecnología) concentran más acuerdos de cashback?
2. **Comparativa de acuerdos:** ¿Qué plataformas consiguen los porcentajes de devolución más altos para el usuario?
3. **Canales de integración:** ¿Las marcas prefieren ofrecer cashback mediante extensiones de navegador o apps móviles?
4. **Valoración del usuario:** ¿Existe relación entre la cantidad de marcas asociadas a una app y su calificación (rating)?
5. **Análisis Geográfico:** ¿En qué países de Europa se conoce, se usa más y se genera mayor volumen de transacciones?
6. **Perfil demográfico:** ¿Cuál es el perfil de usuario (edad, género, frecuencia) que más utiliza estos servicios?
7. **Oportunidades de mercado:** ¿Qué sectores o países tienen baja competencia pero altos márgenes para lanzar nuevas plataformas?

---

## 📊 Dataset Utilizado
* **Origen:** Datos basados en informes reales de la industria (Awin, iGraal, Rakuten) combinados con comportamiento demográfico Fintech.
* **Volumen:** +1,500 transacciones simuladas de manera hiperrealista.
* **Variables clave:** `ID_Transaccion`, `Fecha`, `Cliente_Edad`, `Pais`, `Marca`, `Categoria`, `Plataforma_Cashback`, `Porcentaje_Devolucion`, `Canal_Integracion`, `Monto_Compra`.

---

## 🛠️ Problemas de Calidad de Datos Identificados (A limpiar)
Para simular un entorno real de ingeniería de datos, el dataset original contiene las siguientes imperfecciones que se corrigen en el pipeline:
* **Formatos mezclados:** Porcentajes expresados como texto (`"3,5%"`) y como decimales (`0.035`).
* **Inconsistencias de texto:** Países y categorías con problemas de mayúsculas/minúsculas y espacios (`"España"`, `"espana"`, `"ES "`).
* **Valores faltantes (NaN):** Registros nulos en perfiles de usuario y porcentajes de devolución para simular falta de tracking.
* **Duplicados:** Transacciones repetidas por errores de sincronización de servidores.

---

## 🗂️ Estructura del Repositorio
```text
▼ mi-proyecto-modular1/
  ▼ data/
    ├── raw/                  # CSV original con imperfecciones
    └── processed/            # CSV limpio generado por el pipeline
  ▼ notebooks/
    └── eda_analisis.ipynb    # Cuaderno de investigación y análisis exploratorio (EDA)
  ▼ reports/
    └── figures/              # Gráficos e insights exportados (PNG)
  ▼ src/
    ├── __init__.py           # Inicializador de módulo Python
    ├── io.py                 # Funciones de carga y exportación de archivos
    ├── cleaning.py           # Funciones de limpieza y transformación de datos
    └── viz.py                # Funciones de generación y guardado de gráficos
  ├── main.py                 # Orquestador del pipeline completo
  ├── requirements.txt        # Dependencias del proyecto
  └── README.md               # Documentación general
```

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Activar el entorno virtual:**
   ```bash
   source .venv/bin/activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar el pipeline completo:**
   ```bash
   python3 main.py
   ```
   *Esto procesará los datos de `data/raw/`, guardará el archivo limpio en `data/processed/` y exportará los gráficos a `reports/figures/`.*
