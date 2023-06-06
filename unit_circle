import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_unit_circle():
    angles = np.linspace(0, 2*np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-', label='Unit Circle')
    plt.plot([0, 1], [0, 0], 'r-', label='Cosine')
    plt.plot([0, 0], [0, 1], 'g-', label='Sine')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Unit Circle: Sin and Cos')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def main():
    st.title('Unit Circle: Sin and Cos')
    plot_unit_circle()

if __name__ == '__main__':
    main()
