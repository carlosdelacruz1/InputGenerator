import pandas as pd

# Definir los datos
data_hemograma = {
    "Variable": ["Recuento de glóbulos rojos", "Hemoglobina", "Hematocrito", "Volumen corpuscular medio (VCM)", "Hemoglobina corpuscular media (HCM)", "Concentración de hemoglobina corpuscular media (CHCM)",
                 "Recuento de glóbulos blancos (leucocitos)", "Recuento de neutrófilos", "Recuento de linfocitos", "Recuento de monocitos", "Recuento de eosinófilos", "Recuento de basófilos",
                 "Recuento de plaquetas", "Volumen plaquetario medio (VPM)", "Amplitud de distribución de plaquetas (PDW)", "Recuento absoluto de neutrófilos (RAN)", "Recuento absoluto de linfocitos (RAL)",
                 "Recuento absoluto de monocitos (RAM)", "Recuento absoluto de eosinófilos (RAE)", "Recuento absoluto de basófilos (RAB)", "Índice de distribución de glóbulos rojos (RDW)",
                 "Índice neutrófilo-linfocito (NLR)", "Índice plaquetario-linfocito (PLR)", "Índice monocito-linfocito (MLR)"],
    "Descripción": ["Número total de glóbulos rojos en una unidad de volumen de sangre",
                    "Proteína que transporta oxígeno en la sangre",
                    "Proporción de glóbulos rojos en la sangre",
                    "Tamaño promedio de los glóbulos rojos",
                    "Cantidad promedio de hemoglobina en los glóbulos rojos",
                    "Concentración promedio de hemoglobina en los glóbulos rojos",
                    "Número total de glóbulos blancos en una unidad de volumen de sangre",
                    "Número total de neutrófilos en una unidad de volumen de sangre",
                    "Número total de linfocitos en una unidad de volumen de sangre",
                    "Número total de monocitos en una unidad de volumen de sangre",
                    "Número total de eosinófilos en una unidad de volumen de sangre",
                    "Número total de basófilos en una unidad de volumen de sangre",
                    "Número total de plaquetas en una unidad de volumen de sangre",
                    "Tamaño promedio de las plaquetas",
                    "Variabilidad en el tamaño de las plaquetas",
                    "Número absoluto de neutrófilos en una unidad de volumen de sangre",
                    "Número absoluto de linfocitos en una unidad de volumen de sangre",
                    "Número absoluto de monocitos en una unidad de volumen de sangre",
                    "Número absoluto de eosinófilos en una unidad de volumen de sangre",
                    "Número absoluto de basófilos en una unidad de volumen de sangre",
                    "Ancho de la distribución de glóbulos rojos",
                    "Relación entre el número de neutrófilos y linfocitos",
                    "Relación entre el número de plaquetas y linfocitos",
                    "Relación entre el número de monocitos y linfocitos"],
                    "Limite Inferior H": [70, 5.7, 13.8, 38.3, 0.84, 200, 100, 40, 150, 3.4, 6.0, 3.4, 8, 7, 44, 0.2, 20, 100, 50, 20, 1.28, 2, 15, 25],
                    "Limite Superior H": [100, 5.8, 17.2, 48.6, 1.21, 300, 200, 80, 170, 7.0, 8.3, 5.4, 48, 56, 147, 1.2, 30, 200, 60, 30, 3.28, 4, 18, 30],
                    "Limite Inferior M": [70, 5., 12.1, 35.5, 0.84, 200, 100, 50, 150, 2.4, 6.0, 3.4, 8, 7, 44, 0.2, 20, 100, 50, 20, 1.28, 2, 15, 25],
                    "Limite Superior M": [100, 5.8, 15.1, 44.9, 1.21, 300, 200, 100, np.nan, 6.0, 8.3, 5.4, 48, 56, 147, 1.2,  30, 200, 60, 30, 3.28, 4, 18, 30],
                     }
# Crear un DataFrame
df_hemograma = pd.DataFrame(data_hemograma)
df_hemograma.to_csv("Hemograma.csv", index=False)
df_hemograma.to_excel("Hemograma2.xlsx", index=False)


# Reemplazar np.nan con un valor predeterminado
df_hemograma["Limite Superior H"].fillna(9999, inplace=True)
df_hemograma["Limite Superior M"].fillna(9999, inplace=True)


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
df_hemograma["Valor_Aleatorio Hombres"] = df_hemograma.apply(lambda row: generar_valor_aleatorio_hombres(4.25, row["Limite Inferior H"], row["Limite Superior H"]), axis=1)
df_hemograma["Valor_Aleatorio Mujeres"] = df_hemograma.apply(lambda row: generar_valor_aleatorio_mujeres(1.5, row["Limite Inferior M"], row["Limite Superior M"]), axis=1)




# Mostrar el DataFrame
df_hemograma.head(20)
