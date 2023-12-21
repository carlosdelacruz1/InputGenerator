# Secuencia de ADN de ejemplo
secuencia_adn = "ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"

# 1. Conteo de nucleótidos
conteo_nucleotidos = {nucleotido: secuencia_adn.count(nucleotido) for nucleotido in "ATCG"}
print("Conteo de nucleótidos:", conteo_nucleotidos)

# 2. Complemento de la secuencia
complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
secuencia_complemento = "".join(complemento[n] for n in secuencia_adn)
print("Complemento de la secuencia:", secuencia_complemento)

# 3. Traducción a proteína (usando una tabla de traducción ficticia)
tabla_de_traduccion = {"ATG": "M", "TAA": "*", "TAG": "*", "TGA": "*"}
codones = [secuencia_adn[i:i+3] for i in range(0, len(secuencia_adn), 3)]
proteina = "".join(tabla_de_traduccion.get(codon, "X") for codon in codones)
print("Secuencia de proteína:", proteina)

# 4. Generación de fragmentos (fragmentos de 10 bases)
fragmentos = [secuencia_adn[i:i+10] for i in range(0, len(secuencia_adn), 10)]
print("Fragmentos de 10 bases:", fragmentos)

# 5. Búsqueda de motivos
motivo_buscar = "AGCTA"
posiciones = [i for i in range(len(secuencia_adn)) if secuencia_adn.startswith(motivo_buscar, i)]
print(f"Posiciones del motivo '{motivo_buscar}': {posiciones}")

# 6. Reversión de la secuencia
secuencia_reversa = secuencia_adn[::-1]
print("Secuencia revertida:", secuencia_reversa)

# 7. Cálculo de la longitud
longitud = len(secuencia_adn)
print("Longitud de la secuencia:", longitud)

# 8. Generación de secuencias aleatorias (de longitud 30)
import random
import string

secuencia_aleatoria = ''.join(random.choice("ATCG") for _ in range(30))
print("Secuencia de ADN aleatoria:", secuencia_aleatoria)

