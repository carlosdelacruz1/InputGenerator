import pandas as pd
import numpy as np

## Creador de limites para las enfermedades

# Definir las variables
variables = ["Recuento de glóbulos rojos", "Hemoglobina", "Hematocrito", "Volumen corpuscular medio (VCM)", "Hemoglobina corpuscular media (HCM)", "Concentración de hemoglobina corpuscular media (CHCM)",
             "Recuento de glóbulos blancos (leucocitos)", "Recuento de neutrófilos", "Recuento de linfocitos", "Recuento de monocitos", "Recuento de eosinófilos", "Recuento de basófilos",
             "Recuento de plaquetas", "Volumen plaquetario medio (VPM)", "Amplitud de distribución de plaquetas (PDW)", "Recuento absoluto de neutrófilos (RAN)", "Recuento absoluto de linfocitos (RAL)",
             "Recuento absoluto de monocitos (RAM)", "Recuento absoluto de eosinófilos (RAE)", "Recuento absoluto de basófilos (RAB)", "Índice de distribución de glóbulos rojos (RDW)",
             "Índice neutrófilo-linfocito (NLR)", "Índice plaquetario-linfocito (PLR)", "Índice monocito-linfocito (MLR)", "Glucosa en ayunas", "Hemoglobina A1c", "Hemoglobina", "Hematocrito", "Creatinina",
             "Colesterol total", "LDL (colesterol 'malo')", "HDL (colesterol 'bueno')", "Triglicéridos",
             "Ácido úrico", "Proteína total", "Albúmina", "AST", "ALT", "Fosfatasa alcalina", "Bilirrubina total"]

# Crear un DataFrame con valores de ejemplo
data = {
    "Variable": variables,
    "Valor_Sospecha_Diabetes": [
        5.5,  # Recuento de glóbulos rojos (fuera del rango normal)
        15,   # Hemoglobina (fuera del rango normal)
        50,   # Hematocrito (fuera del rango normal)
        100,  # VCM (fuera del rango normal)
        35,   # HCM (fuera del rango normal)
        32,   # CHCM (fuera del rango normal)
        11000,  # Recuento de glóbulos blancos (fuera del rango normal)
        80,   # Recuento de neutrófilos (fuera del rango normal)
        20,   # Recuento de linfocitos (fuera del rango normal)
        700,  # Recuento de monocitos (fuera del rango normal)
        300,  # Recuento de eosinófilos (fuera del rango normal)
        50,   # Recuento de basófilos (fuera del rango normal)
        600000,  # Recuento de plaquetas (fuera del rango normal)
        15,   # VPM (fuera del rango normal)
        18,   # PDW (fuera del rango normal)
        8000,  # RAN (fuera del rango normal)
        1500,  # RAL (fuera del rango normal)
        500,  # RAM (fuera del rango normal)
        100,  # RAE (fuera del rango normal)
        30,   # RAB (fuera del rango normal)
        16,   # RDW (fuera del rango normal)
        5,    # NLR (fuera del rango normal)
        100,  # PLR (fuera del rango normal)
        2,    # MLR (fuera del rango normal)
        120,  # Glucosa en ayunas (fuera del rango normal)
        8.5,  # Hemoglobina A1c (fuera del rango normal)
        18,   # Hemoglobina (fuera del rango normal)
        55,   # Hematocrito (fuera del rango normal)
        1.5,  # Creatinina (fuera del rango normal)
        250,  # Colesterol total (fuera del rango normal)
        160,  # LDL (fuera del rango normal)
        30,   # HDL (fuera del rango normal)
        200,  # Triglicéridos (fuera del rango normal)
        7.5,  # Ácido úrico (fuera del rango normal)
        8.0,  # Proteína total (fuera del rango normal)
        3.0,  # Albúmina (fuera del rango normal)
        80,   # AST (fuera del rango normal)
        60,   # ALT (fuera del rango normal)
        150,  # Fosfatasa alcalina (fuera del rango normal)
        1.2   # Bilirrubina total (fuera del rango normal)
    ]
}

df_sospecha_diabetes = pd.DataFrame(data)
print(df_sospecha_diabetes)

