import pandas as pd
import matplotlib.pyplot as plt

# === Paso 1: Cargar los datos ===
archivo = 'datos.csv'  # Cambia esto si tu archivo tiene otro nombre o ruta

try:
    df = pd.read_csv(archivo)
    print(f"✅ Archivo '{archivo}' cargado correctamente.\n")
except FileNotFoundError:
    print(f"❌ Error: El archivo '{archivo}' no se encontró.")
    exit()

# === Paso 2: Mostrar las primeras filas ===
print("📌 Primeras 5 filas del dataset:")
print(df.head(), "\n")

# === Paso 3: Resumen estadístico ===
print("📊 Resumen estadístico de columnas numéricas:")
print(df.describe(include='all'), "\n")

# === Paso 4: Revisión de valores nulos ===
print("🔍 Valores nulos por columna:")
print(df.isnull().sum(), "\n")

# === Paso 5: Tipos de datos por columna ===
print("🔠 Tipos de datos:")
print(df.dtypes, "\n")

# === Paso 6: Visualización con histogramas ===
print("📈 Generando histogramas de columnas numéricas...")
df.select_dtypes(include='number').hist(figsize=(10, 8), bins=20)
plt.suptitle('Distribución de columnas numéricas', fontsize=14)
plt.tight_layout()
plt.show()
