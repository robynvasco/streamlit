import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def proportional_relationship(x, y):
    # Calculate the proportional relationship
    k = y[0] / x[0]
    return k

def visualize_proportional_relationship(x, y):
    # Create a scatter plot to visualize the proportional relationship
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue')
    
    k = proportional_relationship(x, y)
    ax.plot(x, k * np.array(x), color='red', linestyle='--')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Proportional Relationship')

    st.pyplot(fig)

def main():
    st.title("Proportional Relationship Visualization")

    st.write("The proportional relationship is a key concept in the Rule of Three. It represents a direct relationship between two quantities where the ratio between them is constant.")

    x = st.multiselect("Select values for 'x':", options=[1, 2, 3, 4, 5])
    y = [2, 4, 6, 8, 10]

    if st.button("Visualize"):
        visualize_proportional_relationship(x, y)

if __name__ == "__main__":
    main()
