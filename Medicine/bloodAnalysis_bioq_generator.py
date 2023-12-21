###Creador Bioquimica
import numpy as np
import pandas as pd

# Definir los datos
data = {
    "Variable": ["Glucosa en ayunas", "Hemoglobina A1c", "Hemoglobina", "Hematocrito", "Creatinina",
                 "Colesterol total", "LDL (colesterol 'malo')", "HDL (colesterol 'bueno')", "Triglicéridos",
                 "Ácido úrico", "Proteína total", "Albúmina", "AST", "ALT", "Fosfatasa alcalina", "Bilirrubina total"],
    "Descripción": ["Niveles de glucosa en sangre en ayunas",
                    "Refleja el control de azúcar a largo plazo",
                    "Proteína que transporta oxígeno en la sangre",
                    "Proporción de glóbulos rojos en la sangre",
                    "Indica la función renal",
                    "Niveles totales de colesterol en sangre",
                    "Lipoproteína de baja densidad",
                    "Lipoproteína de alta densidad",
                    "Niveles de grasa en la sangre",
                    "Producto de desecho del metabolismo",
                    "Medida de proteínas en suero",
                    "Proteína producida por el hígado, indica función hepática",
                    "Enzima hepática",
                    "Enzima hepática",
                    "Enzima producida por hígado y huesos",
                    "Pigmento amarillo producido por descomposición de glóbulos rojos"],
    "Limite Inferior H": [70, 5.7, 13.8, 38.3, 0.84, 200, 100, 40, 150, 3.4, 6.0, 3.4, 8, 7, 44, 0.2],
    "Limite Superior H": [100, 5.8, 17.2, 48.6, 1.21, 300, 200, 80, 170, 7.0, 8.3, 5.4, 48, 56, 147, 1.2],
    "Limite Inferior M": [70, 5., 12.1, 35.5, 0.84, 200, 100, 50, 150, 2.4, 6.0, 3.4, 8, 7, 44, 0.2],
    "Limite Superior M": [100, 5.8, 15.1, 44.9, 1.21, 300, 200, 100, np.nan, 6.0, 8.3, 5.4, 48, 56, 147, 1.2],
}
# Crear un DataFrame
df = pd.DataFrame(data)
df.to_csv("analisis.csv", index=False)
df.to_excel("analisis2.xlsx", index=False)

# Reemplazar np.nan con un valor predeterminado
df["Limite Superior H"].fillna(9999, inplace=True)
df["Limite Superior M"].fillna(9999, inplace=True)


# Función para generar valores aleatorios por encima o por debajo de los límites con porcentaje de diferencia
def generar_valor_aleatorio_hombres(porcentaje_diferencia, limite_inferior_H, limite_superior_H):
    # Calcular la diferencia permitida
    diferencia = (limite_superior_H - limite_inferior_H) * porcentaje_diferencia 
    
    # Generar un valor aleatorio dentro de la diferencia y ajustarlo a los límites
    valor_aleatorio = np.random.uniform(-diferencia, diferencia)
    valor_aleatorio = np.clip(valor_aleatorio, limite_inferior_H, limite_superior_H)
    
    return valor_aleatorio

def generar_valor_aleatorio_mujeres(porcentaje_diferencia, limite_inferior_M, limite_superior_M):
    # Calcular la diferencia permitida
    diferencia = (limite_superior_M - limite_inferior_M) * porcentaje_diferencia
    
    # Generar un valor aleatorio dentro de la diferencia y ajustarlo a los límites
    valor_aleatorio = np.random.uniform(-diferencia, diferencia)
    valor_aleatorio = np.clip(valor_aleatorio, limite_inferior_M, limite_superior_M)
    
    return valor_aleatorio

# Aplicar la función a cada fila del DataFrame y almacenar el resultado en una nueva columna "Valor_Aleatorio"
#porcentaje_diferencia = 0.1  # Puedes ajustar este valor según tus preferencias
df["Valor_Aleatorio Hombres"] = df.apply(lambda row: generar_valor_aleatorio_hombres(4.25, row["Limite Inferior H"], row["Limite Superior H"]), axis=1)
df["Valor_Aleatorio Mujeres"] = df.apply(lambda row: generar_valor_aleatorio_mujeres(1.5, row["Limite Inferior M"], row["Limite Superior M"]), axis=1)

# Mostrar el DataFrame
#print(df)
df.head(20)

