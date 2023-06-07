import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Arc

# Set seaborn style
sns.set_style('white')

# Set custom color palette
custom_palette = ['#F53B57', '#00A8FF', '#00B894']
sns.set_palette(custom_palette)

def plot_unit_circle(alpha):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(15, 7))
    plt.subplot(1, 2, 1)
    plt.plot([0, x], [0, 0], '-', linewidth=3, color=custom_palette[0], label='cos')
    plt.plot([x, x], [0, y], '-', linewidth=3, color=custom_palette[1], label='sin')
    plt.plot([0, x], [0, y], '-', linewidth=3, color=custom_palette[2], label='Radius')
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
    plt.text(x/2, -0.1, 'cos', ha='center', va='bottom', fontsize=12, color=custom_palette[0])
    plt.text(x+0.1, y/2, 'sin', ha='center', va='bottom', fontsize=12, color=custom_palette[1])

    # Draw the angle arc and annotate the angle value in degrees
    angle_degrees = np.degrees(alpha)
    arc = Arc((0, 0), 1, 1, 0, 0, angle_degrees, color=custom_palette[2], linewidth=1)
    plt.gca().add_patch(arc)
    angle_text = f"\u03B1={int(angle_degrees)}\u00B0"
    plt.text(0.5, 0.15, angle_text, ha='center', va='center', fontsize=10, color='black')
    
    
     # Plot the sine and cos function
    plt.subplot(1, 2, 2)
    plt.plot(np.linspace(0, 2*np.pi, 100), np.sin(np.linspace(0, 2*np.pi, 100)), color=custom_palette[1], linewidth=2)
    plt.scatter(alpha, y, color=custom_palette[1], s=50)
    plt.plot([alpha, alpha], [0, y], '-', color=custom_palette[1], linewidth=2)
  

    plt.plot(np.linspace(0, 2*np.pi, 100), np.cos(np.linspace(0, 2*np.pi, 100)), color=custom_palette[0], linewidth=2)
    plt.scatter(alpha, x, color=custom_palette[0], s=50)
    plt.plot([alpha, alpha], [0, x], '-', color=custom_palette[0], linewidth=2)
    tick_values = np.linspace(0, 2*np.pi, 5)
    tick_labels = ['0', 'π/2', 'π', '3π/2', '2π']
    plt.xticks(tick_values, tick_labels)
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.xlabel('alpha')
    plt.ylabel('y')
    plt.ylim(-1.5, 1.5)
    plt.title('Sine and Cosine Functions', fontsize=18, fontweight='bold')
    plt.legend(loc='upper right', fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.5)
    

    st.pyplot(plt)
    
    
def fraction_html(numerator, denominator):
    return f'<div>{numerator}</div><div style="border-top:1px solid black;padding-top:2px">{denominator}</div>'

def main():
    st.title('Unit Circle and Trigonometric Functions')
    alpha = st.slider('Select the angle \u03B1 in \u00B0', 0, 360, 45)
    alpha_rad = np.radians(alpha)
    plot_unit_circle(alpha_rad)
    
    st.write('')
    st.write('### Trigonometric Values')
    table_data = {
        '': ['α in degrees', 'α in radians', 'sin(α)', 'Memory Aid for sin(α)', 'cos(α)'],
        '0°': ['0', '0', '0', '½', '1'],
        '30°': ['30', 'π/6', '½', '½√1', '1/2√3'],
        '45°': ['45', 'π/4', '1/2√2', '1/2√2', '1/2√2'],
        '60°': ['60', 'π/3', '1/2√3', '1/2√3', '1/2'],
        '90°': ['90', 'π/2', '1', '1/2√4', '0']
    }


    st.table(table_data)


if __name__ == '__main__':
    main()
