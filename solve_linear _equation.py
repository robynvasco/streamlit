import streamlit as st

def solve_linear_equation():
    st.title("Linear Equation Solver Game")
    st.write("Welcome to the Linear Equation Solver Game! Let's practice solving linear equations together.")

    # Generate a linear equation and its solution
    equation, solution = generate_linear_equation()

    # Display the equation to the user
    st.header("Solve the following equation:")
    st.latex(equation)

    # Collect the user's steps to solve the equation
    steps = []
    while True:
        user_input = st.text_input("Enter your next step:")
        if user_input:
            steps.append(user_input)
        else:
            break

    # Check if the user's steps lead to the correct solution
    is_solution_correct = check_solution(steps, equation, solution)

    # Display the results to the user
    st.header("Results")
    if is_solution_correct:
        st.success("Congratulations! Your solution is correct.")
    else:
        st.error("Oops! Your solution is incorrect.")

def generate_linear_equation():
    # Generate a linear equation in the form ax + b = c
    a = st.random.randint(-10, 10)
    b = st.random.randint(-10, 10)
    c = st.random.randint(-10, 10)

    equation = f"{a}x + {b} = {c}"
    solution = (c - b) / a

    return equation, solution

def check_solution(steps, equation, solution):
    # Evaluate the user's steps and check if they lead to the correct solution
    x = None
    try:
        for step in steps:
            exec(step, globals())
        x_correct = eval('x')
    except:
        return False

    return x_correct == solution

solve_linear_equation()
