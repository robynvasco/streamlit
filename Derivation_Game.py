import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Set up Streamlit layout
st.title("Function Derivation Game")

# Function input
st.sidebar.title("Function Input")
function_input = st.sidebar.text_input("Enter a function (e.g., x^2 + 3*x + 2)", "x^2 + 3*x + 2")

# Derivation level input
st.sidebar.title("Derivation Level")
derivation_level = st.sidebar.slider("Select derivation level", 1, 5, 1)

# Generate derivative function
x = sp.symbols('x')
function = sp.sympify(function_input)
derivative = function
for _ in range(derivation_level):
    derivative = sp.diff(derivative, x)

# Generate x and y values for plotting
x_vals = np.linspace(-10, 10, 100)
y_vals = [sp.lambdify(x, function)(val) for val in x_vals]
y_der_vals = [sp.lambdify(x, derivative)(val) for val in x_vals]

# Plot the original function and its derivative
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label="Original Function")
ax.plot(x_vals, y_der_vals, label="Derivative Function")
ax.legend()

# Display the plot
st.pyplot(fig)

# Display the derivative function
st.subheader("Derivative Function")
st.latex(sp.latex(derivative))
