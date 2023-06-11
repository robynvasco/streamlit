import streamlit as st
import sympy as sp

def apply_term(equation, term):
    x = sp.symbols('x')
    if term.isnumeric():
        term_expr = sp.Rational(int(term))
        new_equation = sp.Add(equation.lhs, term_expr) == equation.rhs
    else:
        term_expr = sp.sympify(term)  # Parse the term as a symbolic expression
        new_equation = equation + term_expr
    new_equation = sp.simplify(new_equation)
    return new_equation

def main():
    st.title("Equation Manipulator")
    equation = sp.Eq((sp.symbols('x') + 3) / 15 + 3, 5)
    
    st.subheader("Initial Equation:")
    st.latex(sp.latex(equation))

    term = st.text_input("Enter a term to apply to both sides of the equation:")
    if st.button("Apply Term"):
        if term:
            equation = apply_term(equation, term)
            st.subheader("Updated Equation:")
            st.latex(sp.latex(equation))

if __name__ == "__main__":
    main()
