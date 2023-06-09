import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def visualize_proportional_bridge(a, b, c, x):
    fig, ax = plt.subplots()
    
    # Plot known values
    ax.plot([0, 1], [0, a], color='blue', label='a')
    ax.plot([0, 1], [0, c], color='red', label='c')
    
    # Plot unknown value
    ax.plot([1, 2], [a, x], color='green', label='x')
    
    # Plot bridge lines
    ax.plot([1, 1], [a, c], color='gray', linestyle='--')
    ax.plot([1, 2], [c, c], color='gray', linestyle='--')
    
    # Add labels and annotations
    ax.text(-0.1, a, 'a', ha='right', va='center')
    ax.text(-0.1, c, 'c', ha='right', va='center')
    ax.text(2.1, x, 'x', ha='left', va='center')
    ax.text(0.5, (a + c) / 2, 'b', ha='center', va='center')
    
    ax.set_xlim([-0.5, 2.5])
    ax.set_ylim([0, max(a, c, x) * 1.2])
    ax.set_xlabel('Bridge')
    ax.set_ylabel('Values')
    ax.set_title('Proportional Bridge')
    ax.legend()

    return fig

def main():
    st.title("Rule of Three Visualization")

    st.write("The Rule of Three is a mathematical principle that allows you to solve problems based on proportions. Given three known values, you can calculate the unknown value using the formula: (a / b = c / x)")

    a = st.number_input("Enter value for 'a':", value=1, min_value=1, step=1)
    b = st.number_input("Enter value for 'b':", value=1, min_value=1, step=1)
    c = st.number_input("Enter value for 'c':", value=1, min_value=1, step=1)

    if st.button("Calculate"):
        x = (b * c) / a
        st.write(f"The unknown value 'x' is: {x}")

        fig = visualize_proportional_bridge(a, b, c, x)

        st.pyplot(fig)

if __name__ == "__main__":
    main()
