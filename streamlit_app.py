import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Define the function to plot
def plot_graph(a):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(a * x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of y = sin({a}*x)')
    plt.grid(True)
    st.pyplot(plt)

# Main function to run the app
def main():
    st.title("Graph of y = sin(a*x)")
    a = st.slider('Select a value for "a"', 0, 10, 5)
    plot_graph(a)

if __name__ == '__main__':
    main()

