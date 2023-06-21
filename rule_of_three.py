import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, a], [0, b], '-', color='#CCCCCC', solid_capstyle='round')
    ax.plot([0, c], [0, x], '-', color='#CCCCCC', solid_capstyle='round')
    ax.plot([0, c], [0, 0], '-', color='#7FDBFF', linewidth=3, label=f'Map Distance c = {c} cm', solid_capstyle='round')
    ax.plot([c, c], [0, x], '-', color='#00B894', linewidth=3, label=f'Real Distance x = {x} km', solid_capstyle='round')
    ax.plot([0, a], [0, 0], '-', color='#00BFFF', linewidth=3, label=f'Map Distance a = {a} cm', solid_capstyle='round')
    ax.plot([a, a], [0, b], '-', color='#006F5F', linewidth=3, label=f'Real Distance b = {b} km', solid_capstyle='round')
    
  
    
    # Add labels
    ax.text(a/2, -0.7, "a", ha='center', va='bottom', color='#00BFFF')
    ax.text(a-0.1, b/2, "b", ha='right', va='center', color='#006F5F')
    ax.text(c-0.5, -0.7, "c", ha='center', va='bottom', color='#7FDBFF')
    ax.text(c-0.1, x/2, "x", ha='right', va='center', color='#00B894')
    
    # Set plot limits
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 16)
   
    
    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')
    
    # Show legend
    ax.legend(fontsize='small')
    
    ax.text(1, -1, r'$\frac{a}{b} = \frac{2}{3}$', ha='left', va='bottom', fontsize=12, usetex=True)
    ax.text(5, -1, r'$\frac{c}{x} = \frac{' + str(c) + r'}{' + str(round(x, 2)) + r'}$', ha='left', va='bottom', fontsize=12, usetex=True)
   
    
    # Show plot
    st.pyplot(fig)

def main():
    st.title('Rule of Three')
    
    # Constants
    a = 2
    b = 3
    
    # Calculate x
    x = lambda c: (b * c) / a
    
    # User input for c
    c = st.slider('Map Distance c in cm', min_value=1, max_value=10, value=4)
    
    # Calculate distance
    distance = x(c)
    
    # Print distance
    st.write("If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
    st.write(f"A distance of {c} cm on the map is equivalent to a real distance of {distance} km.")
    
    # Plot triangle
    plot_triangle(a, b, c)

if __name__ == '__main__':
    main()
