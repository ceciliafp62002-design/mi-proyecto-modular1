import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker

# Inicializar librerías y asegurar reproducibilidad
fake = Faker(['es_ES'])
np.random.seed(42)
random.seed(42)

# 1. PARÁMETROS REALES DE LA INDUSTRIA (MUESTRA)
marcas_sectores = {
    'Viajes': ['Booking', 'Expedia', 'Renfe', 'Iberia', 'Vueling'],
    'Moda': ['Nike', 'Zalando', 'ASOS', 'Zara', 'Mango', 'Sephora'],
    'Tecnología': ['PcComponentes', 'Apple', 'Amazon', 'MediaMarkt', 'Fnac'],
    'Alimentación': ['Carrefour', 'Dia', 'Uber Eats', 'Just Eat']
}

plataformas = ['iGraal', 'Letyshops', 'Awin_Affiliate', 'Revolut_Rewards']
canales = ['Extensión Navegador', 'App Móvil', 'Web/Enlace Directo']

# Distribución geográfica
paises_realistas = ['España', 'España', 'España', 'Francia', 'Alemania', 'Reino Unido', 'Italia']
generos = ['F', 'M', 'No binario']

datos = []

# 2. GENERACIÓN DE 1,500 FILAS
for i in range(1500):
    id_transaccion = f"TRX-2026-{i+1:04d}"
    
    # Fecha en el último año
    fecha_base = datetime(2026, 6, 13)
    fecha_trx = fecha_base - timedelta(days=random.randint(0, 365))
    
    # Demografía realista (Concentrado en 25-45 años)
    edad = int(np.random.normal(loc=34, scale=8))
    edad = max(18, min(edad, 75)) 
    
    genero = random.choice(generos)
    pais = random.choice(paises_realistas)
    
    # Selección de marca y sector
    sector = random.choice(list(marcas_sectores.keys()))
    marca = random.choice(marcas_sectores[sector])
    
    plataforma = random.choice(plataformas)
    canal = random.choice(canales)
    
    # Monto de compra según el sector
    if sector == 'Viajes':
        monto = round(random.uniform(80.0, 650.0), 2)
        tasa_base = random.uniform(0.03, 0.07)
    elif sector == 'Moda':
        monto = round(random.uniform(25.0, 150.0), 2)
        tasa_base = random.uniform(0.04, 0.10)
    elif sector == 'Tecnología':
        monto = round(random.uniform(40.0, 900.0), 2)
        tasa_base = random.uniform(0.01, 0.03)
    else: 
        monto = round(random.uniform(15.0, 80.0), 2)
        tasa_base = random.uniform(0.02, 0.05)

    # 3. INYECCIÓN DE SUCIEDAD CONTROLADA
    
    # Error A: Mezcla de formatos de Porcentaje (Texto con coma vs Decimal)
    if random.random() < 0.4:
        porcentaje_dev = f"{str(round(tasa_base * 100, 1)).replace('.', ',')}%"
    else:
        porcentaje_dev = str(round(tasa_base, 4))
        
    # Error B: Inconsistencias de texto en Países
    if pais == 'España':
        pais = random.choice(['España', 'espana', 'ES', 'España '])
        
    # Error C: Inconsistencias de texto en Categorías/Sectores
    if random.random() < 0.15:
        sector = sector.lower().strip()
        
    # Error D: Valores Nulos
    if random.random() < 0.05:
        porcentaje_dev = np.nan
    if random.random() < 0.03:
        edad = np.nan

    datos.append([id_transaccion, fecha_trx.strftime('%Y-%m-%d'), edad, genero, pais, marca, sector, plataforma, canal, monto, porcentaje_dev])

# Crear DataFrame
columnas = ['ID_Transaccion', 'Fecha', 'Cliente_Edad', 'Cliente_Genero', 'Pais', 'Marca', 'Categoria', 'Plataforma_Cashback', 'Canal_Integracion', 'Monto_Compra', 'Porcentaje_Devolucion']
df = pd.DataFrame(datos, columns=columnas)

# Error E: Filas Duplicadas corregido (cambiado random.seed por random_state)
duplicados = df.sample(n=45, random_state=42)
df = pd.concat([df, duplicados], ignore_index=True)

# Guardar
df.to_csv('data/raw/cashback_transactions_raw.csv', index=False)
print("¡Dataset sintético corregido y generado con éxito!")
