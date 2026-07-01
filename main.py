
import requests
from src.scraping_code import extraer_marcas, extraer_cashback

web= "https://es.igraal.com/marcas/"
respuesta = requests.get(web)
html_content = respuesta.text
marcas = extraer_marcas(html_content)
cashback_marcas = extraer_cashback(html_content)
print (marcas, cashback_marcas)

print(respuesta.status_code)
print(len(respuesta.text))
print(respuesta.text[:500])
