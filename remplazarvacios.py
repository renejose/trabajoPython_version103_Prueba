import pandas as pd

# Cargar el archivo CSV (ajusta el nombre de archivo)
df = pd.read_csv('archivo.csv')

# Mostrar valores antes del reemplazo
print("Antes del reemplazo:")
print(df)

# Reemplazar celdas en blanco (espacios vacíos o celdas vacías) por 0
df.replace(r'^\s*$', 0, regex=True, inplace=True)

# Convertir columnas numéricas si es necesario (puede generar NaN si hay texto)
df = df.apply(pd.to_numeric, errors='ignore')

# Mostrar valores después del reemplazo
print("\nDespués del reemplazo:")
print(df)

# (Opcional) Guardar el DataFrame limpio
df.to_csv('archivo_limpio.csv', index=False)
