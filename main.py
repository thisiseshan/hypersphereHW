import streamlit as st
import numpy as np
import math
from scipy.special import gamma
import plotly.express as px

def hyperviz(dimensions, r, n):
    fractions = []
    calculated_fractions = []
    for d in dimensions:
        points = np.random.uniform(-r, r, (n, d))
        distances = np.linalg.norm(points, axis=1)
        fraction = np.sum(distances <= r) / n
        fractions.append(fraction)

        calculated_fraction = np.pi ** (d * 0.5) / (2 ** d * gamma(d * 0.5 + 1))
        calculated_fractions.append(calculated_fraction)

    return fractions, calculated_fractions


def plotter(dimensions, fractions, calculated_fractions, title):
    dimensions_list = list(dimensions)
    fig = px.line(title=title)
    fig.add_scatter(x=dimensions_list, y=fractions, mode='lines', name='Computed Fraction')
    fig.add_scatter(x=dimensions_list, y=calculated_fractions, mode='lines', name='Theoretical Value', line=dict(dash='dash'))
    fig.update_layout(xaxis_title='Dimension', yaxis_title='Fraction of Points Inside Hypersphere')
    st.plotly_chart(fig)


st.title('Hypersphere Visualization')
st.subheader('DS5220 Homework 1 Question 7c')
st.sidebar.header('Parameters')
n = st.sidebar.slider('Number of Points (n)', 50, 2000, 1000, 50)
r = st.sidebar.slider('Radius (r)', 1, 100000, 1, 1)
dimensions = range(1, st.sidebar.slider('Max Dimension', 10, 200, 100, 10) + 1)

fractions, calculated_fractions = hyperviz(dimensions, r, n)
plotter(dimensions, fractions, calculated_fractions, f"Plot: r={r}, n={n}")