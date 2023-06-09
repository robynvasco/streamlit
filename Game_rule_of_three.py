import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def rule_of_three_calculator(a, b, c):
    x = (b * c) / a
    return x

def visualize_proportional_relationship(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue')
    k = y[0] / x[0]
    ax.plot(x, k * np.array(x), color='red', linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Proportional Relationship')

    return fig

def visualize_direct_proportionality(a, b):
    values = [a, b]
    labels = ['a', 'b']
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Values')
    ax.set_ylabel('Area')
    ax.set_title('Direct Proportionality - Area Model')

    return fig

def visualize_direct_proportional_slope(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    slope = (y[1] - y[0]) / (x[1] - x[0])
    ax.annotate(f"Slope = {slope}", xy=(x[0], y[0]), xytext=(0, 5), textcoords='offset points', ha='center')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Direct Proportional Slope')

    return fig

def main():
    st.title("Rule of Three Visualization")

    st.write("The Rule of Three is a mathematical principle that allows you to solve problems based on proportions. Given three known values, you can calculate the unknown value using the formula: (a / b = c / x)")

    a = st.number_input("Enter value for 'a':", value=1, min_value=1, step=1)
    b = st.number_input("Enter value for 'b':", value=1, min_value=1, step=1)
    c = st.number_input("Enter value for 'c':", value=1, min_value=1, step=1)

    if st.button("Calculate"):
        x = rule_of_three_calculator(a, b, c)
        st.write(f"The unknown value 'x' is: {x}")

        x_values = [a, c]
        y_values = [b, x]

        fig1 = visualize_proportional_relationship(x_values, y_values)
        fig2 = visualize_direct_proportionality(a, b)
        fig3 = visualize_direct_proportional_slope(x_values, y_values)

        st.pyplot(fig1)
        st.pyplot(fig2)
        st.pyplot(fig3)

if __name__ == "__main__":
    main()
