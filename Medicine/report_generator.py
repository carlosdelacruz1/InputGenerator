##Generar informe
# Definir valores de referencia para el hipoparatiroidismo (ficticio)
rango_calcio = [8.5, 10.5]
rango_fosforo = [2.5, 4.5]
rango_pth = [10, 65]

# Ejemplo de informe médico ficticio para un paciente con hipoparatiroidismo
informe_hipoparatiroidismo = """
INFORME MÉDICO

Fecha: {fecha_actual}
Paciente ID: {paciente_id}
Nombre: {nombre_paciente}
Edad: {edad_paciente}
Género: {genero_paciente}

Diagnóstico: Hipoparatiroidismo

Se ha realizado un análisis de sangre al paciente para evaluar diferentes parámetros, y los resultados sugieren la presencia de hipoparatiroidismo. Los valores fuera de rango son los siguientes:

- Calcio en sangre: {valor_calcio} (rango normal: {rango_calcio[0]} - {rango_calcio[1]})
- Fósforo en sangre: {valor_fosforo} (rango normal: {rango_fosforo[0]} - {rango_fosforo[1]})
- Hormona paratiroidea (PTH): {valor_pth} (rango normal: {rango_pth[0]} - {rango_pth[1]})

Recomendaciones:
1. Es recomendable que el paciente consulte con su médico de cabecera para una evaluación clínica más detallada.
2. Se aconseja realizar pruebas adicionales, como una prueba de confirmación específica para el hipoparatiroidismo (por ejemplo, medición de autoanticuerpos o una gammagrafía paratiroidea).
3. Seguir cualquier recomendación y tratamiento proporcionado por el médico para abordar el hipoparatiroidismo.

Es importante destacar que este informe es puramente ficticio y no debe considerarse como un diagnóstico médico real. Consulte con profesionales de la salud para obtener información precisa y personalizada.
"""

# Sustituir valores ficticios en el informe
informe_final = informe_hipoparatiroidismo.format(
    fecha_actual="07 de diciembre de 2023",
    paciente_id=123,
    nombre_paciente="Juan Pérez",
    edad_paciente=35,
    genero_paciente="Masculino",
    valor_calcio=8.0,
    valor_fosforo=2.0,
    valor_pth=8.5,
    rango_calcio=rango_calcio,
    rango_fosforo=rango_fosforo,
    rango_pth=rango_pth
)

# Imprimir el informe final
print(informe_final)

