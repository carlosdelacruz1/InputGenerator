'''
Archivo GenBank de ejemplo ficticio

LOCUS       NC_123456789 987654321 bp ds-DNA circular
DEFINITION  Ejemplo de archivo GenBank con anotaciones detalladas.
ACCESSION   NC_123456789
VERSION     NC_123456789.1
KEYWORDS    GenBank; secuencia genómica; anotación; ejemplo.

SOURCE      Organismo Hipoteticus
  ORGANISM  Organismo Hipoteticus
            Eukaryota; Hypotheticae; Hypothetica; Hypotheticae.

REFERENCE   1  (bases 1 to 987654321)
  AUTHORS   Investigador, A.
  TITLE     "Secuencia Genómica Completa de Organismo Hipoteticus"
  JOURNAL   Genomics 123, 4567-7890 (2023)
  PUBMED    12345678

COMMENT     Anotaciones adicionales pueden ir aquí.

FEATURES             Location/Qualifiers
     gene            100..400
                     /gene="Gen1"
                     /locus_tag="ABC123"
                     /note="Gen importante"
     CDS             100..400
                     /gene="Gen1"
                     /locus_tag="ABC123"
                     /product="Proteína A"
                     /translation="MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGL
                     NPKSHIIYVGDANIVGGDGNKARELIEELFRKIYKDFP"

     gene            complement(600..800)
                     /gene="Gen2"
                     /locus_tag="DEF456"
                     /note="Gen menos importante"
     CDS             complement(600..800)
                     /gene="Gen2"
                     /locus_tag="DEF456"
                     /product="Proteína B"
                     /translation="MKLTITIAGGGTRKRRPLRKGILSKAFKEDYGAQLHMDPHVVCLH
                     AGKSKRIEGYLLAEFDKGTDTDIYLV"
                     
     repeat_region    2000..2200
                     /note="Repetición en la secuencia"
                     
     tRNA            3500..3600
                     /gene="tRNA-Ala"
                     /product="ARNt-Ala"
                     
     misc_feature    5000..5500
                     /note="Característica miscelánea"
                     /experiment="experimental"
                     /function="importante"
                     
ORIGIN
        1 gattcaatgg cattagatcc tccttgggca cgtgctgtag atctcgtctc ctggtcaaca
       61 aaaaaaaaat agctttgctg agagctgtca gagcggcctc ataggcgagg agtttgcatt
      ... (987654321 bases) ...
//
''' 
