import control
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import plotly.graph_objects as go

def rlocusyc(G):
    # Calcular el lugar de las raíces
    rlist, klist = rlocus(G)
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

