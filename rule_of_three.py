import streamlit as st
import matplotlib.pyplot as plt

def plot_triangle(a, b, c):
    # Plot triangle
    plt.plot([0, a], [0, 0], color='green', label='b')
    plt.plot([a, a], [0, b], color='blue', label='a')
    plt.plot([0, a], [0, b], color='grey')
    plt.plot([0, c], [0, 0], color='red')
    plt.plot([c, c], [0, (a*c)/b], color='red')
    
    # Add labels
    plt.text(a/2, 0, f'a = {a}', ha='center', va='bottom')
    plt.text(a, b/2, f'b = {b}', ha='right', va='center')
    
    # Set plot limits
    plt.xlim(0, max(a, c) + 1)
    plt.ylim(0, max(b, (a*c)/b) + 1)
    
    # Show legend
    plt.legend()
    
    # Show plot
    st.pyplot()

def main():
    st.title('Rule of Three')
    
    # Constants
    a = 2
    b = 3
    
    # Calculate x
    x = lambda c: (a * c) / b
    
    # User input for c
    c = st.slider('c', min_value=1, max_value=10, value=5)
    
    # Calculate distance
    distance = x(c)
    
    # Print distance
    st.write(f"The real distance between the two points on the map that are 5 cm apart is: {distance} km")
    
    # Plot triangle
    plot_triangle(a, b, c)

if __name__ == '__main__':
    main()
