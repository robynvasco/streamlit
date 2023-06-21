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
    a = 20
    b = 10

    # Calculate c
    c = lambda x: (a * b) / x

    st.info("At a farm, it takes 10 days for 20 ducks to eat the food that’s left out for them. How much time would it take for a different number of ducks to eat the same food?")
    # User input for x
    x = st.slider('Number of Ducks (x)', min_value=1, max_value=30, value=20)

    # Calculate c
    new_c = c(x)

    # Plot subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Proportional Relationship: a * b = c * x', fontsize=16)

    # Plot a * b
    axes[0].bar(0, a * b, color='orange')
    axes[0].text(0, a * b + 1, str(a * b), ha='center')
    axes[0].set_ylim(0, a * b + 10)
    axes[0].set_xlim(-1, 1)
    axes[0].set_axis_off()
    axes[0].set_title('a * b')

    # Plot c * x
    axes[1].bar(0, new_c * x, color='orange')
    axes[1].text(0, new_c * x + 1, str(new_c * x), ha='center')
    axes[1].set_ylim(0, new_c * x + 10)
    axes[1].set_xlim(-1, 1)
    axes[1].set_axis_off()
    axes[1].set_title('c * x')

    # Adjust subplot spacing
    plt.tight_layout()

    # Show plot
    st.pyplot(fig)

    st.write("")
    answer = st.text_input("How many ducks would it take to eat the same food in the given time? Enter your answer for c (number of ducks):", placeholder="Type your answer here, e.g., 15")
    if answer:
        try:
            if float(answer) == new_c:
                st.success(f"That's correct! It would take approximately {new_c} ducks to eat the same food in {x} days.")
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
