import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Arc
import pandas as pd

# Set seaborn style
sns.set_style('white')

# Set custom color palette
custom_palette = ['#F53B57', '#00A8FF', '#00B894']
sns.set_palette(custom_palette)

def plot_unit_circle(alpha, show_sine=True, show_cosine=True):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(15, 7))
    plt.subplot(1, 2, 1)
    plt.plot([0, x], [0, 0], '-', linewidth=3, color=custom_palette[0], label=r'$\cos(\alpha)$' if show_cosine else None)
    plt.plot([x, x], [0, y], '-', linewidth=3, color=custom_palette[1], label=r'$\sin(\alpha)$' if show_sine else None)
    plt.plot([0, x], [0, y], '-', linewidth=3, color=custom_palette[2], label='Radius=1')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), '--', linewidth=1, color='gray', alpha=0.5, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.yticks([])
    plt.yticks([-1, 0, 1])
    plt.axis('off')
    plt.title('Unit Circle', fontsize=18, fontweight='bold')
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.gca().set_aspect('equal')  # Set aspect ratio to equal

    # Draw floating labels for sin and cos lines
    plt.text(x/2, -0.1, r'$\cos(\alpha)$', ha='center', va='bottom', fontsize=12, color=custom_palette[0] if show_cosine else 'none')
    plt.text(x+0.2, y/2, r'$\sin(\alpha)$', ha='center', va='bottom', fontsize=12, color=custom_palette[1] if show_sine else 'none')

    # Draw the angle arc and annotate the angle value in degrees
    angle_degrees = np.degrees(alpha)
    arc = Arc((0, 0), 1, 1, 0, 0, angle_degrees, color="grey", linewidth=2)
    plt.gca().add_patch(arc)
    angle_text = r'$\alpha={}$'.format(int(angle_degrees)) + r'$^\circ$'
    plt.text(0.3, 0.15, angle_text, ha='center', va='center', fontsize=10, color='grey')

    ######### Plot the sine and cosine functions
    if show_sine:
        plt.subplot(1, 2, 2)
        plt.plot(np.linspace(0, 2*np.pi, 100), np.sin(np.linspace(0, 2*np.pi, 100)), color=custom_palette[1], linewidth=2)
        plt.scatter(alpha, y, color=custom_palette[1], s=50)
        plt.plot([alpha, alpha], [0, y], '-', color=custom_palette[1], linewidth=3)

    if show_cosine:
        plt.plot(np.linspace(0, 2*np.pi, 100), np.cos(np.linspace(0, 2*np.pi, 100)), color=custom_palette[0], linewidth=2)
        plt.scatter(alpha, x, color=custom_palette[0], s=50)
        plt.plot([alpha, alpha], [0, x], '-', color=custom_palette[0], linewidth=2)

    tick_values = np.linspace(0, 2*np.pi, 5)
    tick_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
    plt.xticks(tick_values, tick_labels)
    tick_values = np.array([-1,-np.sqrt(3)/2,-np.sqrt(2)/2,-1/2,0,1/2,np.sqrt(2)/2,np.sqrt(3)/2,1])
    tick_labels = ['-1', r'$-\frac{\sqrt{3}}{2}$', r'$-\frac{\sqrt{2}}{2}$', r'$-\frac{1}{2}$', '0', r'$\frac{1}{2}$', r'$\frac{\sqrt{2}}{2}$', r'$\frac{\sqrt{3}}{2}$', '1']
    plt.yticks(tick_values, tick_labels)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-1.5, 1.5)
    plt.title('Sine and Cosine Functions', fontsize=18, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.5)

    st.pyplot(plt)


def main():
    st.title('Unit Circle and Trigonometric Functions')
    alpha = st.slider('Select the angle α in degrees', 0, 360, 45)
    alpha_rad = np.radians(alpha)

    show_sine = st.checkbox('Show Sine', value=True)
    show_cosine = st.checkbox('Show Cosine', value=True)

    plot_unit_circle(alpha_rad, show_sine, show_cosine)

    st.write('')
    st.write('### Trigonometric Values')
    table_data = {
        'α in degrees': ['0°', '30°', '45°', '60°', '90°'],
        'α in radians': ['0', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$'],
        'sin(α)': ['0', r'$\frac{1}{2}$', r'$\frac{\sqrt{2}}{2}$', r'$\frac{\sqrt{3}}{2}$', '1'],
        'Memory Aid for sin(α)': [r'$\sqrt{0}/2$', r'$\sqrt{1}/2$', r'$\sqrt{2}/2$', r'$\sqrt{3}/2$', r'$\sqrt{4}/2$'],
        'cos(α)': ['1', r'$\frac{\sqrt{3}}{2}$', r'$\frac{\sqrt{2}}{2}$', r'$\frac{1}{2}$', '0']
    }

    df = pd.DataFrame(table_data)

    # Render the table
    st.table(df)


if __name__ == '__main__':
    main()
