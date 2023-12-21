import pandas as pd

# Definir límites para cada columna
limites = {
    'radiacion_solar': (0, 300),
    'eficiencia_reactor': (0, 100),
    'eficiencia_sistema_biologico': (0, 100),
    'eficiencia_separacion': (0, 100),
}

# Generar datos aleatorios para cada columna
datos = {}
for columna, (limite_inferior, limite_superior) in limites.items():
    datos[columna] = np.random.uniform(limite_inferior, limite_superior, size=1000)

# Crear DataFrame
df_chemistry = pd.DataFrame(datos)
print(df_chemistry.head())  # Corregir nombre del DataFrame aquí

# Definir función para asignar etiquetas en función de los valores
def asignar_etiqueta(row):
    # Ejemplo de asignación de etiquetas en función de los valores
    if row['radiacion_solar'] > 250 and row['eficiencia_reactor'] > 90 and row['eficiencia_sistema_biologico'] > 90 and row['eficiencia_separacion'] > 90:
        return 'alta'
    elif row['radiacion_solar'] < 150 and row['eficiencia_reactor'] < 30 and row['eficiencia_sistema_biologico'] < 30 and row['eficiencia_separacion'] < 30:
        return 'bajo'
    else:
        return 'medio'

# Aplicar la función a la columna 'Etiqueta'
df_chemistry['CO2 conversion'] = df_chemistry.apply(asignar_etiqueta, axis=1)

# Guardar DataFrame en formato CSV
df_chemistry.to_csv('dataset.csv', index=False)

print(df_chemistry.head())  # Corregir nombre del DataFrame aquí

