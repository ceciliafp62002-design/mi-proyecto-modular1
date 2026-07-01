# Función A — Extraer marcas + slug del listado `/marcas`

from bs4 import BeautifulSoup

def extraer_marcas(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    marcas = []

    # Acotamos al contenedor del directorio (div.ur63mv0),
    # así NO se cuelan las categorías del menú desplegable.
    for a in soup.select('div.ur63mv0 a[href^="/codigos-promocionales/"]'):
        nombre = a.get_text(strip=True)
        slug = a['href'].replace('/codigos-promocionales/', '')
        marcas.append({
            "marca": nombre,
            "slug": slug,
            "url": "https://es.igraal.com" + a['href'],
            "pais": "ES",
        })

    print(f"✔ {len(marcas)} marcas capturadas.")
    return marcas

#⚠️ `ur63mv0` es una clase autogenerada. Si algún día devuelve 0 marcas, hay que volver a inspeccionar la página y actualizar esa clase.

# Función B — Extraer el cashback de una página de tienda

from bs4 import BeautifulSoup
import re

def extraer_cashback(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Nos metemos SOLO en la caja de ofertas reales (ancla estable),
    #    para evitar el "SUPERCASHBACK DEL DÍA" de otras tiendas.
    contenedor = soup.find(attrs={"data-testid": "offer-card-list-container"})
    if not contenedor:
        return None  # la página no tiene ofertas o cambió la estructura

    # 2. Buscamos el primer texto con forma "X % de cashback" dentro de esa caja.
    #    Usamos una expresión regular para no depender de clases frágiles.
    texto = contenedor.get_text(" ", strip=True)
    match = re.search(r'(\d+[.,]?\d*)\s*%\s*de cashback', texto, re.IGNORECASE)

    if match:
        return match.group(1) + "%"   # devuelve "5%"
    return None
