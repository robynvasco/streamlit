import streamlit as st
import matplotlib.pyplot as plt

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    plt.plot([0, a], [0, 0], color='#66C2A5', label='b')  # Green
    plt.plot([a, a], [0, b], color='#8DA0CB', label='a')  # Blue
    plt.plot([0, a], [0, b], color='#A6D854')  # Grey
    plt.plot([0, c], [0, 0], color='#E78AC3')  # Red
    plt.plot([c, c], [0, x], color='#E78AC3')  # Red
    plt.plot([0, c], [0, x], color='#CCCCCC')  # Grey
    
    # Add labels
    plt.text(a/2, 0, f'a = {a}', ha='center', va='bottom')
    plt.text(a, b/2, f'b = {b}', ha='right', va='center')
    
    # Set plot limits
    plt.xlim(0, max(a, c) + 1)
    plt.ylim(0, max(b, x) + 1)
    
    # Hide axes and background
    plt.axis('off')
    plt.gca().set_facecolor('none')
    
    # Show legend
    plt.legend()
    
    # Show plot
    st.pyplot()

def main():
    st.title('Rule of Three')
    st.info("If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
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
    st.write(f"A distance of {c} cm on the map is equivalent to a real distance of {distance} km.")

    
    # Plot triangle
    plot_triangle(a, b, c)

if __name__ == '__main__':
    main()

