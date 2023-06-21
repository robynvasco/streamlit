import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, a], [0, 0], color='#00B894')
    ax.plot([a, a], [0, b], color='#00A8FF')
    ax.plot([0, a], [0, b], color='#F53B57')
    ax.plot([0, c], [0, 0], color='#E78AC3')
    ax.plot([c, c], [0, x], color='#E78AC3')
    ax.plot([0, c], [0, x], color='#CCCCCC')
    
    # Add labels
    ax.text(a/2, 0, f'Map Distance a = {a} cm', ha='center', va='bottom')
    ax.text(a, b/2, f'Real Distance b = {b} km', ha='right', va='center')
    ax.text(c/2, 0, f'Map Distance c = {c} cm', ha='center', va='bottom')
    ax.text(c/2, x/2, f'Real Distance x = {x} km', ha='center', va='center')
    
    # Set plot limits
    ax.set_xlim(0, max(a, c) + 1)
    ax.set_ylim(0, max(b, x) + 1)
    
    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')
    
    # Show legend
    ax.legend()
    
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
    st.write(f"If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
    st.write(f"A distance of {c} cm on the map is equivalent to a real distance of {distance} km.")
    
    # Plot triangle
    plot_triangle(a, b, c)

if __name__ == '__main__':
    main()
    
    import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, a], [0, 0], color='#00B894', label='Map Distance (a)')
    ax.plot([a, a], [0, b], color='#00A8FF', label='Real Distance (b)')
    ax.plot([0, a], [0, b], color='#F53B57', label='Map Distance (c)')
    ax.plot([0, c], [0, 0], color='#E78AC3', label='Real Distance (x)')
    ax.plot([c, c], [0, x], color='#E78AC3')
    ax.plot([0, c], [0, x], color='#CCCCCC')
    
    # Add labels
    ax.text(a/2, 0, f'Map Distance (a) = {a} cm', ha='center', va='bottom')
    ax.text(a, b/2, f'Real Distance (b) = {b} km', ha='right', va='center')
    ax.text(c/2, 0, f'Map Distance (c) = {c} cm', ha='center', va='bottom')
    ax.text(c/2, x/2, f'Real Distance (x) = {x} km', ha='center', va='center')
    
    # Set plot limits
    ax.set_xlim(0, max(a, c) + 1)
    ax.set_ylim(0, max(b, x) + 1)
    
    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')
    
    # Show legend
    ax.legend()
    
    # Show plot
    st.pyplot(fig)

def main():
    st.title('Rule of Three')
    
    # Constants
    map_distance_a = 2
    real_distance_b = 3
    
    # Calculate real distance (x) based on map distance (c)
    real_distance = lambda c: (real_distance_b * c) / map_distance_a
    
    # User input for map distance (c)
    map_distance_c = st.slider('Map Distance (c)', min_value=1, max_value=10, value=5)
    
    # Calculate real distance
    real_distance_x = real_distance(map_distance_c)
    
    # Print distance
    st.write("A scale on the map shows that two centimeters on a map are equivalent to 3 km. Then how far is the real distance between two points on the map that are 5 cm apart?")
    st.write(f"A map distance of {map_distance_c} cm is equivalent to a real distance of {real_distance_x} km.")
    
    # Plot triangle
    plot_triangle(map_distance_a, real_distance_b, map_distance_c)

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()

