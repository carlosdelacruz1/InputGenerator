import numpy as np
import matplotlib.pyplot as plt

# Definir límites inferiores y superiores
limite_inferior = 5
limite_superior = 15

# Generar outliers uniformemente distribuidos dentro de los límites
outliers = np.random.uniform(limite_inferior, limite_superior, 100)

# Graficar los datos
plt.hist(outliers, bins=20, density=True, alpha=0.6, color='r', label='Outliers')
plt.axvline(limite_inferior, color='b', linestyle='dashed', linewidth=2, label='Límite Inferior')
plt.axvline(limite_superior, color='g', linestyle='dashed', linewidth=2, label='Límite Superior')

plt.title('Generación de Outliers entre Límites Inferiores y Superiores')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()


# Definir límites inferiores y superiores
limite_inferior = 5
limite_superior = 15

# Rango para generar outliers (fuera de los límites)
rango_outliers_inferiores = (-10, limite_inferior)
rango_outliers_superiores = (limite_superior, 30)

# Generar outliers uniformemente distribuidos fuera de los límites
outliers_inferiores = np.random.uniform(*rango_outliers_inferiores, 50)
outliers_superiores = np.random.uniform(*rango_outliers_superiores, 50)

# Graficar los datos
plt.hist(outliers_inferiores, bins=20, density=True, alpha=0.6, color='r', label='Outliers Inferiores')
plt.hist(outliers_superiores, bins=20, density=True, alpha=0.6, color='b', label='Outliers Superiores')
plt.axvline(limite_inferior, color='g', linestyle='dashed', linewidth=2, label='Límite Inferior')
plt.axvline(limite_superior, color='y', linestyle='dashed', linewidth=2, label='Límite Superior')

plt.title('Generación de Outliers Fuera de Límites')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

