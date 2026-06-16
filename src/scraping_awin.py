import os
import csv
import requests
from bs4 import BeautifulSoup

def descargar_html(url):
    """Realiza la petición HTTP con User-Agent para evitar bloqueos."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        respuesta = requests.get(url, headers=headers, timeout=10)
        if respuesta.status_code == 200:
            return respuesta.text
        print(f"Error en la descarga. Código de estado: {respuesta.status_code}")
        return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def extraer_ofertas(html_content):
    """Parsea el HTML para extraer marcas y porcentajes de cashback."""
    soup = BeautifulSoup(html_content, 'html.parser')
    lista_marcas = []
    
    # NOTA: Reemplazar estos selectores por los selectores reales de la web objetivo
    bloques_marcas = soup.find_all('div', class_='merchant-card') 
    
    for bloque in bloques_marcas[:40]: # Limitado a las 30-40 marcas requeridas
        try:
            nombre = bloque.find('h3', class_='merchant-name').text.strip()
            cashback = bloque.find('span', class_='cashback-rate').text.strip()
            
            lista_marcas.append({
                "marca": nombre,
                "cashback_ofrecido": cashback,
                "pais": "ES" # O el país analizado
            })
        except AttributeError:
            continue # Ignora bloques malformados para evitar caídas
            
    return lista_marcas

def guardar_datos_raw(datos, nombre_archivo="marcas_raw.csv"):
    """Guarda la lista de diccionarios en la ruta data/raw/."""
    ruta_destino = os.path.join("data", "raw", nombre_archivo)
    
    # Asegura que la estructura de carpetas existe
    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
    
    if not datos:
        print("No hay datos para guardar.")
        return
        
    columnas = datos[0].keys()
    with open(ruta_destino, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(datos)
    print(f"Datos guardados exitosamente en: {ruta_destino}")

def ejecutar_scraping():
    """Flujo principal del script."""
    print("Iniciando adquisición de datos reales...")
    url_objetivo = "https://ejemplo-awin-o-afiliado.com" 
    
    html = descargar_html(url_objetivo)
    if html:
        datos_extraidos = extraer_ofertas(html)
        guardar_datos_raw(datos_extraidos)
    else:
        print("Proceso abortado por fallo en la descarga HTML.")

if __name__ == "__main__":
    ejecutar_scraping()
