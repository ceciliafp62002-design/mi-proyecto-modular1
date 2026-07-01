# 📑 PROMPT DE CONTEXTO: ESTADO DEL PROYECTO CASHBACK
 
## 📝 Resumen del Proyecto y Contexto Actual
Este es un proyecto modular de Análisis de Datos enfocado en el modelo de negocio del **Cashback**. El repositorio está configurado en un Mac utilizando Visual Studio Code, Git y GitHub. El entorno virtual de Python (`.venv`) está instalado de forma aislada y limpia dentro de la subcarpeta raíz del repositorio de GitHub (`mi-proyecto-modular1`).
 
### ✅ Lo que ya está hecho y configurado:
1. **Conexión Git/GitHub:** El repositorio local está perfectamente vinculado al remoto.
2. **Estructura de Carpetas Profesional:** Creada según los requisitos de la tutoría (`data/raw`, `data/processed`, `notebooks`, `reports/figures`, `src/`).
3. **Entorno Virtual (`.venv`):** Operativo en Mac, sincronizado como intérprete en VS Code y con las librerías base instaladas (`pandas`, `matplotlib`, `seaborn`, `notebook`, `faker`).
4. **Archivos Base:** Creados los archivos estructurales (`.gitignore` configurado para omitir el `.venv`, `requirements.txt`, `README.md` detallado con las 7 preguntas de negocio, `main.py`, y los scripts vacíos en `src/`).
5. **Script de Datos Sintéticos:** Se creó y probó con éxito un script funcional (`generar_dataset.py`) para generar datos con la suciedad requerida por la escuela (comas decimales, nulos, países inconsistentes), aunque se ha pausado para priorizar un enfoque con datos reales. **Dejó un residuo activo:** el CSV `cashback_transactions_raw.csv` sigue guardado en `data/raw/` (ver Día 4).
---
 
## 🛑 ¿Dónde nos hemos quedado? (Día 1)
Nos hemos quedado justo en el punto de inicio de la fase de **Adquisición de Datos**. Hemos validado las reglas del archivo `robots.txt` de la red de afiliación Awin (comprobando que permite el raspado) y hemos definido una **estrategia mixta de datos reales** para asegurar la máxima calidad técnica sin penalizar el tiempo de entrega.
 
---
 
# Día 2
### ✅ Lo que ya está hecho y configurado:
1. **Infraestructura Base:** Conexión Git/GitHub correcta, entorno virtual operativo en VS Code y estructura de carpetas profesional creada (`data/raw`, `data/processed`, `notebooks`, `src/`).
2. **Archivos de Control:** `.gitignore`, `requirements.txt` y `README.md` estructurados con las 7 preguntas de negocio.
3. **Estrategia de Datos Modificada:** Se ha **descartado por completo el uso de datos sintéticos (`Faker`)**. El proyecto utilizará una **Estrategia Mixta de Datos Reales**: Marcas reales obtenidas por scraping + volumen transaccional real obtenido de plataformas analíticas externas.
4. **Fase 1 (Web Scraping - Paso A) Completada y Cerrada:**
   * Se creó el script modular `src/scraping_code.py`.
   * Se creó la bitácora educativa `notebooks/01_adquisicion_datos.ipynb`.
   * **Práctica e Inspección Real:** Se realizó la inspección HTML/CSS en vivo sobre la plataforma real **iGraal España**. Se identificó el comportamiento de su arquitectura web y se capturó la clase del contenedor padre (`nalu verticalbasecardlite`).
   * **Código Blindado:** Se programó y documentó el script de extracción final utilizando funciones lambda capaces de esquivar las clases dinámicas comprimidas por el servidor.
   * **Bloqueo detectado (añadido Día 4):** iGraal está protegida con **Cloudflare / sistema antibot**. El scraping con `requests` + `BeautifulSoup` no puede pasar de la página de verificación — no es un problema de selectores CSS, es un bloqueo a nivel de red/JavaScript. Para conseguir extraer contenido real de esta web haría falta **Selenium** (o herramienta equivalente que controle un navegador real), lo cual queda pendiente como aprendizaje futuro, no resuelto en este proyecto por ahora.
### 🧠 Conceptos clave aprendidos y documentados para repasar:
* **Estructuras Multi-Plataforma:** Uso de diccionarios de configuración (`config_redes`) y bucles con `.items()` para automatizar la extracción de múltiples redes (Awin, CJ Affiliate, Rakuten, Impact) con una sola función inteligente.
* **Consolidación de Datos:** Uso de `.extend()` en lugar de `.append()` para fusionar listas de diccionarios en un único nivel plano sin anidar listas.
* **Compresión en Next.js:** Comprensión de cómo los frameworks web modernos inyectan hashes alfanuméricos aleatorios (ej: `_16sh3nb0`) en las clases CSS y cómo combatirlos aislando la raíz de la clase estable.
* **Protección antibot (Cloudflare):** algunas webs modernas bloquean peticiones automatizadas simples independientemente de que los selectores CSS estén bien construidos. Es una barrera distinta a "no encontrar el elemento" — hay que reconocer la diferencia entre ambos problemas.
### 🛑 ¿Dónde nos hemos quedado? (Día 2)
Hemos cerrado con éxito el **Paso A** de la adquisición de datos (Scraping de marcas reales) tras entender cómo mapear elementos en entornos web complejos. Nos hemos quedado justo al inicio del **Paso B**: la conexión e importación automatizada de los datasets transaccionales masivos mediante APIs.
 
---
 
# Día 3
 
### ✅ Lo que ya está hecho y configurado:
1. **Ruta de adquisición decidida (Paso B):** Se descartó Hugging Face y se eligió la **API de Kaggle**.
2. **Dataset transaccional elegido:** `iamsouravbanerjee/customer-shopping-trends-dataset` (~3.900 registros de compra por cliente; datos sintéticos; cumple el requisito de >1.000 filas). El identificador con formato `owner/slug` es lo que usa la API para localizarlo.
3. **Módulo de descarga creado (`src/data_acquisition.py`):** función `descargar_dataset_kaggle(slug, destino)` que autentica con Kaggle y descarga + descomprime el CSV en `data/raw/`. Coherente con la arquitectura modular: la lógica reutilizable vive en `src/`, y el notebook solo la importa, ejecuta y narra.
4. **Bitácora del notebook montada (`notebooks/01_adquisicion_datos.ipynb`):** celdas de teoría (token + permisos), celda de `sys.path` para poder importar `src/`, celda de descarga, celda de verificación (`os.listdir`) y celda de carga + diagnóstico inicial (`shape`, `head`).
5. **Token de Kaggle configurado (SISTEMA NUEVO):** Kaggle ya **no** entrega un `kaggle.json` a `Downloads`. Ahora, al pulsar *Generate New Token*, genera un token de texto `KGAT_...` que se guarda en `~/.kaggle/access_token`. Configurado con éxito mediante:
```bash
   mkdir -p ~/.kaggle && echo KGAT_... > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token
```
   El antiguo `kaggle.json` figura ahora como "Legacy API Credentials".
 
### 🧠 Conceptos clave aprendidos y documentados para repasar:
* **Token:** credencial (usuario + clave secreta) que te identifica ante Kaggle sin escribir la contraseña cada vez. La librería lo lee desde `~/.kaggle/` al llamar a `api.authenticate()`.
* **Permisos Unix (`chmod 600`):** en Mac/Linux cada archivo define quién puede leer/escribir (dueño / grupo / otros). Un token debe ser legible solo por su dueño (`600` = dueño lee+escribe, grupo nada, otros nada). Si está abierto a otros, Kaggle lo rechaza por seguridad.
* **`sys.path` y por qué el notebook no encontraba `src`:** Python busca los módulos a importar solo dentro de una lista de carpetas (`sys.path`), que por defecto incluye la carpeta desde donde se ejecuta. El notebook corre desde `notebooks/`, así que no ve `src/` (está un nivel arriba). Se soluciona añadiendo la raíz del proyecto al `sys.path`.
* **`__init__.py`:** archivo (puede estar vacío) que convierte una carpeta en un paquete importable. `src/` lo necesita para que funcione `from src.data_acquisition import ...`.
## 🛑 ¿Dónde nos hemos quedado? (Día 3)
Token nuevo de Kaggle ya colocado en `~/.kaggle/access_token`. Pendiente de verificar que la librería de Python lee correctamente este token nuevo. La descarga real del dataset aún no se había ejecutado.
 
---
 
# Día 4
 
### ✅ Lo que ya está hecho y configurado:
1. **Autenticación de Kaggle verificada:** `kaggle datasets list -s "customer shopping trends"` devolvió una tabla de resultados → el token nuevo (`access_token`) se lee correctamente.
2. **Descarga de Kaggle ejecutada con éxito:** se corrió `descargar_dataset_kaggle(DATASET, RAW_DIR)` desde el notebook y devolvió `Dataset URL: https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset` + la ruta de destino confirmada: `/Users/ramon/Desktop/Máster Ceci/mi-proyecto-modular1/data/raw`.
3. **Bug corregido en el notebook:** la celda de `PROJECT_ROOT` tenía escrito el nombre del proyecto en vez de `".."`:
```python
   # ANTES (mal):
   PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), "mi-proyecto-modular1"))
   # AHORA (correcto):
   PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), ".."))
```
   `".."` sube un nivel real desde `notebooks/` hasta la raíz; escribir el nombre del proyecto intenta entrar en una subcarpeta que no existe. Corregido y confirmado funcionando. La línea vieja se dejó comentada como rastro, buena práctica.
4. **Incidencia de kernel resuelta:** apareció un `FileNotFoundError` en `os.getcwd()` — causado porque el kernel de Jupyter pierde la referencia a la carpeta de trabajo si esta se mueve/renombra mientras el kernel sigue abierto. Se resolvió con **Restart del kernel** + reejecutar todas las celdas desde el principio.
5. **Contenido real de `data/raw/` identificado — 3 archivos, no 1:**
   * `cashback_transactions_raw.csv` → **residuo del script de Faker** (Día 1-2, pausado). No proviene de la descarga de Kaggle. No se ha usado ni se ha borrado; queda ahí por si se retoma la idea de datos sintéticos.
   * `shopping_trends.csv` → viene del ZIP de Kaggle.
   * `shopping_trends_updated.csv` → segunda versión del mismo dataset, también dentro del ZIP de Kaggle (el propio autor del dataset publicó las dos versiones).
   * **Pendiente:** decidir cuál de las dos versiones de Kaggle usar, comparando `shape` y `columns` de ambas.
### 🧠 Conceptos clave aprendidos y documentados para repasar:
* **`os.getcwd()`:** devuelve la carpeta desde la que se está ejecutando el código en ese momento ("current working directory"). Equivalente a `pwd` en terminal, pero desde dentro de Python. En un notebook dentro de `notebooks/`, `os.getcwd()` apunta a esa carpeta, no a la raíz del proyecto — de ahí la necesidad de `PROJECT_ROOT`.
* **Por qué falla `os.getcwd()` con `FileNotFoundError`:** si la carpeta de trabajo se mueve/renombra/borra mientras el kernel sigue vivo, el sistema operativo pierde la referencia. Se arregla reiniciando el kernel, no tocando el código.
* **Un dataset de Kaggle puede traer varios CSV dentro del mismo ZIP** — no asumir que solo hay uno. Siempre revisar `os.listdir(RAW_DIR)` completo antes de decidir qué archivo cargar, y no fiarse solo del nombre que uno "espera" encontrar.
* **Separar "residuos de intentos anteriores" de "datos de la fuente actual":** antes de cargar un CSV en `data/raw/`, comprobar de dónde vino realmente (mirar el log/output de la celda que lo generó), no solo el nombre del archivo.
* **Docstrings desactualizados:** el docstring de `descargar_dataset_kaggle()` afirma que `destino` debe ser "ruta absoluta", pero `os.makedirs()` acepta también rutas relativas — el código es menos estricto que lo que promete la documentación. No es un bug, pero es un hábito a vigilar: que los comentarios/docstrings describan lo que el código hace de verdad.
* **Comentarios de código que quedan obsoletos:** las celdas markdown sobre el token de Kaggle en el notebook aún hablan del sistema viejo (`kaggle.json`), cuando el proyecto usa el sistema nuevo (`access_token`). Pendiente de corregir texto explicativo para que no confunda en el futuro (ver más abajo, notebook a revisar).
## 🛑 ¿Dónde nos hemos quedado? (Día 4)
El **Paso B (adquisición vía Kaggle) está técnicamente cerrado**: token autenticado, descarga ejecutada, archivos confirmados en `data/raw/`. Queda pendiente decidir entre `shopping_trends.csv` y `shopping_trends_updated.csv`, y a partir de ahí arranca formalmente el **EDA** (Análisis Exploratorio de Datos) sobre el dataset elegido.
 
---
 
## 🚀 Próximos pasos (siguiente sesión):
 
1. **Cerrar la elección de archivo Kaggle:** comparar `shopping_trends.csv` vs `shopping_trends_updated.csv` con:
```python
   df_v1 = pd.read_csv(os.path.join(RAW_DIR, "shopping_trends.csv"))
   df_v2 = pd.read_csv(os.path.join(RAW_DIR, "shopping_trends_updated.csv"))
   print("shopping_trends.csv:", df_v1.shape)
   print("shopping_trends_updated.csv:", df_v2.shape)
   print(df_v1.columns.tolist())
   print(df_v2.columns.tolist())
```
   Decidir cuál de los dos usar como fuente definitiva para `data/raw/` (hipótesis a confirmar: `_updated` suele ser la versión revisada/con más columnas, pero no darlo por hecho sin comparar).
 
2. **Diagnóstico inicial del dataset elegido** (primer bloque del protocolo de EDA, ya documentado en `apuntes_master_data_science.md`):
```python
   df.shape
   df.info()
   df.head()
   df.describe()
   df.isna().sum()
   df.duplicated().sum()
```
 
3. **Cerrar `data/raw/` como inmutable** una vez decidido el archivo definitivo: a partir de ahí solo se lee, nunca se modifica.
4. **⚠️ REVISAR Y LIMPIAR `notebooks/01_adquisicion_datos.ipynb` — pendiente explícito, no resuelto:**
   El notebook mezcla, en la sección del Paso A (scraping), varios intentos sucesivos escritos en momentos distintos del aprendizaje:
   - Funciones redundantes que hacen prácticamente lo mismo: `extraer_ofertas`, `extraer_ofertas_reales`, `extraer_ofertas_igraal_real`, `extraer_datos_de_red`.
   - URLs de prueba/placeholder mezcladas con el intento real sobre iGraal: `https://ejemplo.com`, `https://httpbin.org`, `https://scrapethissit.com`.
   - Celdas markdown sobre el token de Kaggle que describen el sistema antiguo (`kaggle.json`) en vez del sistema nuevo (`access_token`) que realmente se usa.
   
   **Propuesta para el próximo día:** quedarnos solo con la celda real de iGraal (la que detectó el bloqueo de Cloudflare) + una nota markdown explicando por qué las versiones anteriores fueron intentos de aprendizaje que no llegaron a producción, en vez de dejarlas todas como si fueran pasos necesarios del flujo final. Corregir también el texto sobre el token de Kaggle para que hable del sistema `access_token` real.
5. **Fase de Consolidación e Inyección de "suciedad técnico-académica":** cruzar con Pandas el dataset transaccional con las marcas reales del scraping (Paso A) e introducir de forma controlada los errores exigidos por la escuela (comas decimales erróneas, nulos en campos clave, inconsistencias en nombres de países).
6. **Fase EDA completa (`notebooks/02_eda_analisis.ipynb`):** limpieza con Pandas + `groupby`/`agg` para KPIs + visualizaciones con intención (heatmap de correlación, distribuciones) para responder las 7 preguntas de negocio. Nota: `groupby + agg`, `transform` y `pivot_table` figuran como "pendiente de completar" en `apuntes_master_data_science.md` — serán el próximo bloque de conceptos nuevos a estudiar.
---
 
## ⚙️ Entorno y forma de trabajar (arrastrar a cada sesión)
* **Sistema:** Mac (NO Windows). Shell zsh. Activar el entorno: `source .venv/bin/activate` (verás `(.venv)` en el prompt).
* **Repo:** `mi-proyecto-modular1`, ubicado en `/Users/ramon/Desktop/Máster Ceci/mi-proyecto-modular1`. El notebook vive en `notebooks/`, un nivel por debajo de la raíz → necesita el ajuste de `sys.path` (con `".."`, nunca el nombre del proyecto) para importar `src/`. `src/` necesita `__init__.py`.
* **Kaggle:** sistema NUEVO de token (`KGAT_...` en `~/.kaggle/access_token`), NO el `kaggle.json` de `Downloads`. Ya verificado y funcionando.
* **Método de aprendizaje:** concepto / arquitectura **antes** que el código, siempre. En cada acción, indicar **en qué carpeta**, **qué tipo de archivo** y **por qué**. Ceci teclea el código ella misma. El notebook funciona como bitácora educativa (markdown explicativo + celdas de código).
* **Si `os.getcwd()` da `FileNotFoundError`:** reiniciar el kernel y reejecutar todo desde el principio — no es un error de código.
---
 
## 🧩 Código de referencia producido en la sesión
 
**`src/data_acquisition.py`**
```python
import os
from kaggle.api.kaggle_api_extended import KaggleApi
 
 
def descargar_dataset_kaggle(slug: str, destino: str) -> str:
    """Descarga y descomprime un dataset de Kaggle en la carpeta destino."""
    os.makedirs(destino, exist_ok=True)   # crea data/raw si no existe
    api = KaggleApi()                     # cliente que habla con Kaggle
    api.authenticate()                    # lee el token de ~/.kaggle/access_token
    api.dataset_download_files(slug, path=destino, unzip=True)
    return destino
```
*(Nota pendiente: el comentario original decía "lee ~/.kaggle/kaggle.json" — desactualizado, corregido aquí a `access_token`, que es el sistema real en uso.)*
 
**Celda de `sys.path` del notebook (para importar `src/`) — versión corregida:**
```python
import sys, os
 
PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), ".."))  # ".." = sube un nivel, NUNCA el nombre del proyecto
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
 
from src.data_acquisition import descargar_dataset_kaggle
```
 
**Celda de descarga (ya ejecutada con éxito):**
```python
DATASET = "iamsouravbanerjee/customer-shopping-trends-dataset"
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
descargar_dataset_kaggle(DATASET, RAW_DIR)
```
 
**Celda de verificación (ya ejecutada — resultado real):**
```python
print(os.listdir(RAW_DIR))
# → ['cashback_transactions_raw.csv', 'shopping_trends.csv', 'shopping_trends_updated.csv']
```