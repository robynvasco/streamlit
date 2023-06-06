import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_unit_circle(alpha):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(6, 6))
    plt.plot([0,x], [0, 0], 'g-', linewidth=2, label='cos')
    plt.plot([0,  x], [x, y], 'r-', linewidth=2, label='sin')
    plt.plot([0, x], [0, y], 'b-', linewidth=2, label='Radius')
    plt.plot(x, y, 'bo', label='Point')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), 'gray', linestyle='--', alpha=0.3, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Unit Circle: Sin and Cos')
    plt.legend()
    plt.grid(True)

    # Display the values of sin(alpha) and cos(alpha)
    st.markdown(f"**sin(alpha)**: {y:.4f}")
    st.markdown(f"**cos(alpha)**: {x:.4f}")

    st.pyplot(plt)

def main():
    st.title('Unit Circle: Sin and Cos')
    alpha = st.slider('Select the angle (alpha)', 0.0, 2*np.pi, np.pi/4)
    plot_unit_circle(alpha)

if __name__ == '__main__':
    main()
