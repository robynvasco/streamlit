import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_unit_circle(alpha):
    angles = np.linspace(0, 2*np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)

    # Rotate the unit circle based on the selected angle
    x_rotated = np.cos(alpha) * x - np.sin(alpha) * y
    y_rotated = np.sin(alpha) * x + np.cos(alpha) * y

    # Calculate the values of sin(alpha) and cos(alpha)
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)

    plt.figure(figsize=(6, 6))
    plt.plot(x_rotated, y_rotated, 'b-', label='Rotated Unit Circle')
    plt.plot([0, x_rotated[50]], [0, y_rotated[50]], 'r-', label='Cosine')
    plt.plot([0, x_rotated[0]], [0, y_rotated[0]], 'g-', label='Sine')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Rotated Unit Circle: Sin and Cos')
    plt.legend()
    plt.grid(True)

    # Display the values of sin(alpha) and cos(alpha)
    st.markdown(f"**sin(alpha)**: {sin_alpha:.4f}")
    st.markdown(f"**cos(alpha)**: {cos_alpha:.4f}")

    st.pyplot(plt)

def main():
    st.title('Rotated Unit Circle: Sin and Cos')
    alpha = st.slider('Select the angle (alpha)', 0.0, 2*np.pi, np.pi/4)
    plot_unit_circle(alpha)

if __name__ == '__main__':
    main()

