##Creamos con esto un archivo tipo GenBank de un humano 
# de 1 a 3 mil millones de pares de bases

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import random 

# Longitud deseada de la cadena de ADN
longitud = 1000  

# Probabilidades de aparición de cada base individual (A, T, C, G)
probabilidades_bases = {'A': 0.25, 'T': 0.25, 'C': 0.25, 'G': 0.25}

# Probabilidades de unión de pares de bases
probabilidades_union = {
    ('A', 'T'): 0.4,
    ('T', 'A'): 0.4,
    ('C', 'G'): 0.3,
    ('G', 'G'): 0.1,
    ('G', 'C'): 0.2,
    ('C', 'C'): 0.1,
    ('A','A'): 0.1
}

# Generar la cadena de ADN ficticia
cadena_adn = ''

# Primera base
base_anterior = random.choices(list(probabilidades_bases.keys()), weights=list(probabilidades_bases.values()))[0]
cadena_adn += base_anterior

# Generar las bases restantes teniendo en cuenta las probabilidades de unión
for _ in range(longitud - 1):
    bases_posibles = [base for base in probabilidades_bases.keys() if (base, base_anterior) in probabilidades_union]
    probabilidades = [probabilidades_union[(base, base_anterior)] for base in bases_posibles]
    base_siguiente = random.choices(bases_posibles, weights=probabilidades)[0]
    
    cadena_adn += base_siguiente
    base_anterior = base_siguiente

# Imprimir la cadena de ADN generada
print(cadena_adn)


# Crear un objeto Seq desde la secuencia de ADN
seq_obj = Seq(secuencia_adn)

# Crear un objeto SeqRecord para contener la secuencia y las anotaciones
record = SeqRecord(seq=seq_obj, id="NC_123456789", name="Ejemplo_Secuencia", description="Secuencia de ADN hipotética")

# Agregar anotaciones ficticias
record.annotations["source"] = "Organismo Hipoteticus"
record.annotations["organism"] = "Organismo Hipoteticus"
record.annotations["keywords"] = ["GenBank", "secuencia genómica", "anotación", "ejemplo"]
record.annotations["molecule_type"] = "DNA"  # Agregar el campo molecule_type

# Definir una característica de gen ficticio
gen_feature = SeqFeature(FeatureLocation(start=100, end=400), type="gene")
gen_feature.qualifiers["gene"] = ["Gen1"]
gen_feature.qualifiers["locus_tag"] = ["ABC123"]
gen_feature.qualifiers["note"] = ["Gen importante"]

# Agregar la característica de gen al registro
record.features.append(gen_feature)

# Guardar el registro en un archivo GenBank
with open("secuencia_genbank.gb", "w") as output_file:
    SeqIO.write(record, output_file, "genbank")

print("Archivo GenBank generado exitosamente.")
#print(secuencia_genbank.gb)




