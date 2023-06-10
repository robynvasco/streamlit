import streamlit as st

def solve_linear_equation():
    st.title("Linear Equation Term Identification and Reverse Operation Visualization")
    st.write("Let's practice identifying the terms and reverse operations in linear equations.")

    # Generate a linear equation and its solution
    equation, solution = generate_linear_equation()

    # Display the equation to the user
    st.header("Identify the terms and choose the reverse operation:")
    st.latex(equation)

    # Split the equation into left-hand side and right-hand side
    lhs, rhs = equation.split('=')

    # Split the left-hand side into individual terms
    terms = lhs.split('+')

    # Display the terms and prompt the user to select the reverse operation
    for i, term in enumerate(terms):
        st.write(f"Term {i+1}: {term.strip()}")

    reverse_operation = st.selectbox("Select the reverse operation for the terms:", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Check if the user's selection is correct
    is_selection_correct = check_reverse_operation(reverse_operation, terms, solution)

    # Display the results to the user
    st.header("Results")
    if is_selection_correct:
        st.success("Congratulations! Your selection is correct.")
    else:
        st.error("Oops! Your selection is incorrect.")

def generate_linear_equation():
    # Generate a linear equation in the form ax + b = c
    a = st.random.randint(-10, 10)
    b = st.random.randint(-10, 10)
    c = st.random.randint(-10, 10)

    equation = f"{a}x + {b} = {c}"
    solution = (c - b) / a

    return equation, solution

def check_reverse_operation(selection, terms, solution):
    # Check if the user's selection matches the correct reverse operation
    if selection == "Addition":
        reverse_operation = "+"
    elif selection == "Subtraction":
        reverse_operation = "-"
    elif selection == "Multiplication":
        reverse_operation = "*"
    elif selection == "Division":
        reverse_operation = "/"

    # Check if applying the reverse operation leads to the correct solution
    try:
        for term in terms:
            exec(f"result = x {reverse_operation} {term.strip()}", globals())
    except:
        return False

    return result == solution

solve_linear_equation()
