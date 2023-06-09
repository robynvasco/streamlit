import streamlit as st
import matplotlib.pyplot as plt

def rule_of_three_calculator(a, b, c):
    # Calculate the unknown value using the Rule of Three
    x = (b * c) / a
    return x

def visualize_rule_of_three(a, b, c, x):
    # Create a bar chart to visualize the proportions
    values = [a, b, c, x]
    labels = ['a', 'b', 'c', 'x']

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    ax.annotate(str(a), xy=('a', a), xytext=(0, 5), textcoords='offset points', ha='center')
    ax.annotate(str(b), xy=('b', b), xytext=(0, 5), textcoords='offset points', ha='center')
    ax.annotate(str(c), xy=('c', c), xytext=(0, 5), textcoords='offset points', ha='center')
    ax.annotate(str(round(x, 2)), xy=('x', x), xytext=(0, 5), textcoords='offset points', ha='center')

    ax.set_ylim(0, max(values) * 1.2)
    ax.set_xlabel('Values')
    ax.set_ylabel('Quantity')
    ax.set_title('Rule of Three Visualization')

    st.pyplot(fig)

def main():
    st.title("Rule of Three Visualization")

    st.write("The Rule of Three is a mathematical principle that allows you to solve problems based on proportions. Given three known values, you can calculate the unknown value using the formula: (a / b = c / x)")

    a = st.number_input("Enter value for 'a':", value=1, min_value=1, step=1)
    b = st.number_input("Enter value for 'b':", value=1, min_value=1, step=1)
    c = st.number_input("Enter value for 'c':", value=1, min_value=1, step=1)

    if st.button("Calculate"):
        x = rule_of_three_calculator(a, b, c)
        st.write(f"The unknown value 'x' is: {x}")

        visualize_rule_of_three(a, b, c, x)

if __name__ == "__main__":
    main()
