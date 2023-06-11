import streamlit as st
import sympy as sp

def update_equation(term, operation, equation):
    x = sp.symbols('x')
    if term:
        term_expr = sp.sympify(term)
    else:
        term_expr = 0

    if operation == 'Add':
        updated_equation = equation + term_expr
    elif operation == 'Subtract':
        updated_equation = equation - term_expr
    elif operation == 'Multiply':
        updated_equation = equation * term_expr
    elif operation == 'Divide':
        updated_equation = equation / term_expr
    else:
        updated_equation = equation
    
    return updated_equation

def format_equation(equation):
    return sp.pretty(equation, use_unicode=True)

def main():
    equation = (sp.Symbol('x') + 3) / 15 + 3
    st.title("Equation Calculator")
    st.write(f"Initial equation: {format_equation(equation)}")

    term = st.text_input("Enter a term:")
    operation = st.selectbox("Select an operation:", ['Add', 'Subtract', 'Multiply', 'Divide'])
    equation = update_equation(term, operation, equation)

    st.write(f"Updated equation: {format_equation(equation)}")

if __name__ == '__main__':
    main()
