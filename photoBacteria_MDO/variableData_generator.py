## Ingesta de datos
##3 Leer y limpiar dataset
##3 Generamos medidas del sensor y demas 
import pandas as pd
import numpy as np

# Definir límites para cada columna
## variables
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
df_photo = pd.DataFrame(datos)
print(df_photo.head())

# Guardar DataFrame en formato CSV
df_photo.to_csv('dataset.csv', index=False)
