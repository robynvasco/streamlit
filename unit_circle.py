import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fractions import Fraction

# Set seaborn style
sns.set_style('white')

# Set custom color palette
custom_palette = ['#00B894', '#00A8FF', '#F53B57']
sns.set_palette(custom_palette)

def plot_unit_circle(alpha):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(8, 8))
    plt.plot([0, x], [0, 0], '-', linewidth=3, color=custom_palette[0], label='cos')
    plt.plot([x, x], [0, y], '-', linewidth=3, color=custom_palette[1], label='sin')
    plt.plot([0, x], [0, y], '-', linewidth=3, color=custom_palette[2], label='Radius')
    plt.plot(x, y, 'o', markersize=10, color='black', label='Point')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), '--', linewidth=1, color='gray', alpha=0.5, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.title('Unit Circle: Trigonometric Functions', fontsize=18, fontweight='bold')
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Display the values of sin(alpha) and cos(alpha) in a styled box
    box_style = {
        'boxstyle': 'round',
        'facecolor': 'white',
        'edgecolor': 'gray',
        'linewidth': 1,
        'pad': 0.5
    }
    st.markdown(f"<div style='margin-top: 20px;'><span style='font-size: 16px;'>sin(&alpha;):</span> <span style='font-size: 18px; font-weight: bold; color: {custom_palette[1]};'>{y:.4f}</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='margin-bottom: 20px;'><span style='font-size: 16px;'>cos(&alpha;):</span> <span style='font-size: 18px; font-weight: bold; color: {custom_palette[0]};'>{x:.4f}</span></div>", unsafe_allow_html=True)

    # Draw floating labels for sin and cos lines
    plt.text(x/2, -0.4, 'cos', ha='center', va='bottom', fontsize=12, color=custom_palette[0])
    plt.text(x+0.4, y/2, 'sin', ha='center', va='bottom', fontsize=12, color=custom_palette[1])

    # Annotate the angle alpha
    angle_text = fr"$\alpha = \frac{{{alpha}}}{{\pi}}$"
    plt.annotate(angle_text, (0.05, -0.15), fontsize=14)

    st.pyplot(plt)

def main():
    st.title('Unit Circle: Trigonometric Functions')
    alpha = st.slider('Select the angle (\u03B1)', 0, 16, 4, format='%d * \u03C0/8')
    alpha = alpha * np.pi / 8
    plot_unit_circle(alpha)

if __name__ == '__main__':
    main()
                      
                      
