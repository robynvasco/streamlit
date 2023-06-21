import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    # Colors
    map_color = '#CCCCCC'
    a_color = '#c20420'
    b_color = '#0a6ca8'
    c_color = '#f28d9b'
    x_color = '#accee3'

    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, a], [0, b], '-', color=map_color, solid_capstyle='round')
    ax.plot([0, c], [0, x], '-', color=map_color, solid_capstyle='round')
    ax.plot([0, a], [0, 0], '-', color=a_color, linewidth=3, label=f'Map Distance a = {a} cm', solid_capstyle='round')
    ax.plot([a, a], [0, b], '-', color=b_color, linewidth=3, label=f'Real Distance b = {b} km', solid_capstyle='round')
    ax.plot([0, c], [0, 0], '-', color=c_color, linewidth=5, label=f'Map Distance c = {c} cm', solid_capstyle='round')
    ax.plot([c, c], [0, x], '-', color=x_color, linewidth=3, label=f'Real Distance x', solid_capstyle='round')
    ax.plot([0, a], [0, 0], '-', color=a_color, linewidth=3, solid_capstyle='round')

    # Add labels
    ax.text(a/2, -0.7, "a", ha='center', va='bottom', color=a_color)
    ax.text(a-0.1, b/2, "b", ha='right', va='center', color=b_color)
    ax.text(c-0.5, -0.7, "c", ha='center', va='bottom', color=c_color)
    ax.text(c-0.1, x/2, "x", ha='right', va='center', color=x_color)

    # Set plot limits
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 16)

    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')

    # Show legend
    ax.legend(fontsize='x-small', loc='upper left')

    # Show plot
    st.pyplot(fig)

def rule_of_three():
    st.title('Rule of Three')

    # Constants
    a = 2
    b = 3

    # Calculate x
    x = lambda c: (b * c) / a

    st.info("If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
    # User input for c
    c = st.slider('Map Distance c in cm', min_value=1, max_value=10, value=4)

    # Plot triangle
    plot_triangle(a, b, c)

    # Calculate distance
    distance = x(5)

    # Display formula in st.info
    st.info(f"a is to b as c is to x.\n\n"
            f"$\\frac{{a}}{{b}} = \\frac{{c}}{{x}}$\n")

    with st.expander("Explanation"):
        st.write("The rule of three, also known as the proportionality rule, is a mathematical concept that allows us to solve proportional relationships between different quantities. It is based on the idea that if two ratios are equal, then the corresponding values in those ratios are also equal.")
        st.write("In the sentence 'a is to b as c is to x,' it implies that the ratio of a to b is equal to the ratio of c to x. So in our example, if the distance between two points on the map increases, the real distance also increases proportionally.")
        st.write("To use this sentence, we can interpret it as a mathematical equation:")
        st.latex(r"\frac{a}{b} = \frac{c}{x}")
        st.write("This equation states that the ratio of a to b is equal to the ratio of c to x. It implies that if we know three of the variables, we can calculate the value of the fourth variable.")

    st.write("")
    answer = st.text_input("How far is the real distance between two points on the map that are 5 cm apart? Enter your answer for x in km:", placeholder="Type your answer here, e.g., 3.0 or 4.5")
    if answer:
        try:
            if float(answer) == distance:
                st.success(f"That's correct! A distance of 5 cm on the map is equivalent to a real distance of x = {distance} km.")
            else:
                st.error("That's incorrect. Try again!")
        except ValueError:
            st.error("Invalid input. Please enter a number.")

def inverse_rule_of_three():
    st.title('Inverse Rule of Three')

    # Constants
    a = 2
    c = 5

    # Calculate b
    b = lambda x: (a * x) / c

    st.info("If two centimeters on a map are equivalent to 3 km, what is the distance on the map between two points that are 4 km apart in real life?")
    # User input for x
    x = st.slider('Real Distance x in km', min_value=1, max_value=10, value=3)

    # Plot triangle
    plot_triangle(a, b(x), c)

    # Calculate distance
    distance = b(4)

    # Display formula in st.info
    st.info(f"a is to b as c is to x.\n\n"
            f"$\\frac{{a}}{{b}} = \\frac{{c}}{{x}}$\n")

    with st.expander("Explanation"):
        st.write("The inverse rule of three is used when we want to find a value on one side of the ratio given the value on the other side. In this case, we know the values of a and c, and we want to find the value of b. We can rearrange the equation:")
        st.latex(r"b = \frac{{a \cdot x}}{{c}}")
        st.write("This equation states that the ratio of a to b is equal to the ratio of c to x. By rearranging the equation, we can solve for b.")

    st.write("")
    answer = st.text_input("What is the distance on the map between two points that are 4 km apart in real life? Enter your answer for b in cm:", placeholder="Type your answer here, e.g., 6.0 or 9.5")
    if answer:
        try:
            if float(answer) == distance:
                st.success(f"That's correct! A real distance of 4 km corresponds to a map distance of b = {distance} cm.")
            else:
                st.error("That's incorrect. Try again!")
        except ValueError:
            st.error("Invalid input. Please enter a number.")

def main():
    st.title("Rule of Three and Inverse Rule of Three")
    
    tab1, tab2 = st.tabs(["Rule of Three", "Inverse Rule of Three"])
    
    if tab1:
        rule_of_three()
    elif tab2:
        inverse_rule_of_three()

if __name__ == '__main__':
    main()
