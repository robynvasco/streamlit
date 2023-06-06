import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style('whitegrid')

# Set custom color palette
custom_palette = ['#00B894', '#00A8FF', '#F53B57']
sns.set_palette(custom_palette)

def plot_unit_circle(alpha):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(8, 8))
    plt.plot([0, x], [0, 0], 'o-', linewidth=3, markersize=8, color=custom_palette[0], label='cos')
    plt.plot([x, x], [0, y], 'o-', linewidth=3, markersize=8, color=custom_palette[1], label='sin')
    plt.plot([0, x], [0, y], 'o-', linewidth=3, markersize=8, color=custom_palette[2], label='Radius')
    plt.plot(x, y, 'o', markersize=10, color='black', label='Point')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), '--', linewidth=1, color='gray', alpha=0.5, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title('Unit Circle: Sin and Cos', fontsize=16)
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Display the values of sin(alpha) and cos(alpha)
    st.markdown(f"**sin(alpha)**: {y:.4f}", unsafe_allow_html=True)
    st.markdown(f"**cos(alpha)**: {x:.4f}", unsafe_allow_html=True)

    st.pyplot(plt)

def main():
    st.title('Unit Circle: Sin and Cos')
    alpha = st.slider('Select the angle (alpha)', 0.0, 2*np.pi, np.pi/4)
    plot_unit_circle(alpha)

if __name__ == '__main__':
    main()
