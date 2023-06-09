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
derivation_level = 1

# Point selection for tangent line
st.sidebar.title("Tangent Line")
selected_point = st.sidebar.slider("Select a point", -10.0, 10.0, 0.0)

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

# Calculate tangent line
tangent_line_func = sp.lambdify(x, derivative)(selected_point) * (x - selected_point) + sp.lambdify(x, function)(selected_point)
tangent_line = lambda x_val: tangent_line_func.subs(x, x_val)

# Plot the original function and the tangent line
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(x_vals, y_vals, label="Original Function")
ax1.plot(x_vals, y_der_vals, label="Derivative Function")
ax1.plot(x_vals, [tangent_line(val) for val in x_vals], label="Tangent Line")
ax1.legend()

# Plot the derivative function
ax2.plot(x_vals, y_der_vals, label="Derivative Function")
ax2.legend()

# Set titles and labels for subplots
ax1.set_title("Original Function and Tangent Line")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.set_title("Derivative Function")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# Adjust spacing between subplots
plt.tight_layout()

# Display the plot
st.pyplot(fig)

# Display the derivative function and tangent line equation
st.subheader("Derivative Function")
st.latex(sp.latex(derivative))

st.subheader("Tangent Line Equation")
st.latex(sp.latex(derivative) + "\\cdot (x - " + str(selected_point) + ") + " + sp.latex(function.subs(x, selected_point)))
