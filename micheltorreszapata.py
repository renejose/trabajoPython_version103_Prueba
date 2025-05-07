import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Cargar los datos
archivo = 'datos.csv'  # Cambia esto por el nombre de tu archivo
df = pd.read_csv(archivo)

# Paso 2: Mostrar las primeras filas
print("Primeras 5 filas del dataset:")
print(df.head())

# Paso 3: Resumen estadístico
print("\nResumen estadístico:")
print(df.describe())

# Paso 4: Valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Paso 5: Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Paso 6: Histograma de columnas numéricas
print("\nGenerando histogramas...")
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
