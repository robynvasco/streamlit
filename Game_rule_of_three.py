import streamlit as st
import matplotlib.pyplot as plt

def visualize_direct_proportional_slope(a, b, c, x):
    values = [a, b, c, x]
    labels = ['a', 'b', 'c', 'x']
    fig, ax = plt.subplots()
    ax.plot([1, 2], [a, c], marker='o', label='Known Values')
    ax.annotate(f"Slope = {round((c - a) / (2 - 1), 2)}", xy=(1, a), xytext=(10, 10),
                textcoords='offset points', ha='center')
    ax.set_xlabel('Position')
    ax.set_ylabel('Value')
    ax.set_title('Direct Proportional Slope')
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

        fig3 = visualize_direct_proportional_slope(a, b, c, x)

        st.pyplot(fig3)

if __name__ == "__main__":
    main()
