import pandas as pd
import random
import string

# Crear una lista de 50 ejemplos ficticios de lo que se analiza mediante bioinformática
muestras = [f"Muestra_{i}" for i in range(1, 51)]

# Generar secuencias ficticias de bases para CYD2D6, CYD2C9 y CYD3A4
def generar_secuencia(length):
    return ''.join(random.choice('ACGTU') for _ in range(length))

cyd2d6_sequences = [generar_secuencia(25) for _ in range(50)]  # Ejemplo de secuencias de 20 bases
cyd2c9_sequences = [generar_secuencia(25) for _ in range(50)]  # Ejemplo de secuencias de 20 bases
cyd3a4_sequences = [generar_secuencia(25) for _ in range(50)]  # Ejemplo de secuencias de 20 bases

# Crear un DataFrame con los datos
data = {
    'Muestra': muestras,
    'CYD2D6': cyd2d6_sequences,
    'CYD2C9': cyd2c9_sequences,
    'CYD3A4': cyd3a4_sequences
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
