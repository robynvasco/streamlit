import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Arc

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
    plt.plot(x, y, 'o', markersize=10, color=custom_palette[2], label='Point')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), '--', linewidth=1, color='gray', alpha=0.5, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.title('Unit Circle: Trigonometric Functions', fontsize=18, fontweight='bold')
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Draw floating labels for sin and cos lines
    plt.text(x/2, -0.1, 'cos', ha='center', va='bottom', fontsize=12, color=custom_palette[0])
    plt.text(x+0.1, y/2, 'sin', ha='center', va='bottom', fontsize=12, color=custom_palette[1])

    # Draw the angle arc and annotate the angle value in degrees
    angle_degrees = np.degrees(alpha)
    arc = Arc((0, 0), 1, 1, 0, 0, angle_degrees, color=custom_palette[2], linewidth=1)
    plt.gca().add_patch(arc)
    angle_text = f"Angle: {angle_degrees:.1f}°"
    plt.text(0.5, 0.15, angle_text, ha='center', va='center', fontsize=10, color='black')

    st.pyplot(plt)

def main():
    st.title('Unit Circle: Trigonometric Functions')
    alpha = st.slider('Select the angle (in degrees)', 0, 360, 45)
    alpha_rad = np.radians(alpha)
    plot_unit_circle(alpha_rad)

if __name__ == '__main__':
    main()
