import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1) Importar los datos
    df = pd.read_csv("epa-sea-level.csv")

    # 2) Crear diagrama de dispersión
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Actual data')

    # 3) Línea de regresión para todos los años
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Generar los valores x para la línea hasta 2050
    years_all = pd.Series(range(df['Year'].min(), 2051))
    # Línea de predicción: y = slope * x + intercept
    plt.plot(years_all, res_all.slope * years_all + res_all.intercept,
             color='red', label='Fit: all data')

    # 4) Línea de regresión desde 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.slope * years_recent + res_recent.intercept,
             color='green', label='Fit: 2000 onwards')

    # 5) Etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6) Guardar la figura
    plt.savefig('sea_level_plot.png')
    return plt.gcf()  # Devolver la figura
