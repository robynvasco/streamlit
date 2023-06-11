import streamlit as st
from sympy import Symbol, Eq, simplify

def apply_term_to_equation(equation, term, operator):
    x = Symbol('x')
    equation_term = f'{term} {operator} 0'
    term_expr = eval(equation_term)
    new_equation = Eq(simplify(equation.lhs + term_expr), simplify(equation.rhs + term_expr))
    return new_equation

def main():
    st.title("Equation Manipulator")
    st.write("Start with the equation (x+3)/15+3 = 5")

    # Initial equation
    equation = Eq((Symbol('x') + 3) / 15 + 3, 5)

    # User input
    term_input = st.text_input("Enter a term:")

    # Choose operator
    operator = st.selectbox("Choose an operator:", ('+', '-', '*', '/'))

    # Apply term to equation
    if st.button("Apply Term"):
        new_equation = apply_term_to_equation(equation, term_input, operator)
        equation = new_equation

    st.write(f"Equation: {equation.lhs} = {equation.rhs}")

if __name__ == "__main__":
    main()
