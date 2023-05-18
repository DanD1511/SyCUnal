import control
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import plotly.graph_objects as go

# root_locations

def rlocus_(G):
    # Calcular el lugar de las raíces
    rlist, klist = rlocus(G, plot=False)
    fig = go.Figure()
    # Agregar los puntos correspondientes al lugar de las raíces
    for i in range(len(rlist[0])):
        real_part = np.real(rlist[:, i])
        imag_part = np.imag(rlist[:, i])
        fig.add_trace(go.Scatter(x=real_part, y=imag_part, mode='lines',
                                 name=f'Raíz {i + 1}', hovertemplate='Real: %{x}<br>Imaginaria: %{y}'))
    # Establecer las propiedades del diseño de la gráfica
    fig.update_layout(
        title='Lugar de las Raíces',
        xaxis_title='Parte Real',
        yaxis_title='Parte Imaginaria',
        xaxis_range=[-5, 5],  # Especificar el rango del eje x
        yaxis_range=[-5, 5],  # Especificar el rango del eje y
        plot_bgcolor='white',  # Establecer el color de fondo blanco
        xaxis=dict(gridcolor='lightgray', dtick=1, gridwidth=1, zeroline=False),  # Configurar el eje x
        yaxis=dict(gridcolor='lightgray', dtick=1, gridwidth=1, zeroline=False)  # Configurar el eje y
    )
    # Agregar el hover para mostrar los polos y la ganancia
    fig.update_traces(hovertemplate='Ganancia: %{text}', text=klist.flatten())
    # Mostrar la gráfica interactiva
    fig.show()

##

# period of a marginally stable system

def mssperiod(y, t):
    # Encontrar los índices de los máximos locales
    max_indices = np.where(np.diff(np.sign(np.diff(y))) == -2)[0]

    # Ordenar los máximos locales por magnitud descendente
    sorted_indices = np.argsort(y[max_indices])[::-1]

    # Obtener los índices de los dos máximos consecutivos más altos
    max1_idx = max_indices[sorted_indices[0]]
    max2_idx = max_indices[sorted_indices[1]]

    # Calcular la diferencia entre los tiempos de los dos máximos
    delta_t = t[max1_idx] - t[max2_idx]

    # Mostrar el resultado
    return print(f"el periodo de la onda es de: {delta_t:.2f} segundos")
##

