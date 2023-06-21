import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, c], [0, x], color='#CCCCCC')
    ax.plot([a, a], [0, b], color='#00BFFF', linewidth=2, label=f'Real Distance b = {b} km')
    ax.plot([0, c], [0, 0], color='#00B894', linewidth=4, label=f'Map Distance c = {c} cm')
    ax.plot([c, c], [0, x], color='#7FDBFF', linewidth=2, label=f'Real Distance x = {x} km')
    ax.plot([0, a], [0, 0], color='#006F5F', linewidth=4, label=f'Map Distance a = {a} cm')
  
    
    # Add labels
    ax.text(a/2, 0, "a", ha='center', va='bottom')
    ax.text(a, b/2, "b", ha='right', va='center')
    ax.text(c/2, 0, "c", ha='center', va='bottom')
    ax.text(c, x/2, "x", ha='right', va='center')
    
    # Set plot limits
    ax.set_xlim(0, max(a, c) + 1)
    ax.set_ylim(0, max(b, x) + 1)
    
    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')
    
    # Show legend
    ax.legend(fontsize='small')
    
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
    c = st.slider('c', min_value=1, max_value=10, value=5)
    
    # Calculate distance
    distance = x(c)
    
    # Print distance
    st.write("If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
    st.write(f"A distance of {c} cm on the map is equivalent to a real distance of {distance} km.")
    
    # Plot triangle
    plot_triangle(a, b, c)

if __name__ == '__main__':
    main()
