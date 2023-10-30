import streamlit as st
import numpy as np
import plotly.express as px

def hyperviz(dimensions, r, n):
    fractions = []
    calculated_fractions = []
    for d in dimensions:
        points = np.random.uniform(-r, r, (n, d))
        distances = np.linalg.norm(points, axis=1)
        fraction = np.sum(distances <= r) / n
        fractions.append(fraction)

        calculated_fraction = np.pi ** (d * 0.5) / (2 ** d * np.math.gamma(d * 0.5 + 1))
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
st.subheader('by Eshan Arora')
st.sidebar.header('Parameters')
n = st.sidebar.slider('Number of Points (n)', 50, 2000, 1000, 50)
r = st.sidebar.slider('Radius (r)', 1, 100000, 1, 1)
dimensions = range(1, st.sidebar.slider('Max Dimension', 10, 200, 100, 10) + 1)

fractions, calculated_fractions = hyperviz(dimensions, r, n)
plotter(dimensions, fractions, calculated_fractions, f"Plot: r={r}, n={n}")

st.subheader('Inferences')
st.markdown('1) The fraction of points within the hypersphere decreases sharply as the dimensionality increases. As described in part a, of the problem, this happens due to the curse of dimensionality where the volume of the hyperspace is increasingly concentrated in the corners of the hypercube as dimensionality increases.')
st.markdown('2) When n is sufficiently large, the computed fractions tend to converge to the the theoretival calculated fractions, which is an inficator that our derived formula is correct for large n.')
st.markdown('3) Varying the radius for a fixed dimnension impacts the fraction of points inside the hypersphere but does not change the overall trend seen with varying dimensions. A larger radius will include more points within the hypersphere, but the relative fraction compared to the hypercube continues to decrease with increasing dimensions.')
