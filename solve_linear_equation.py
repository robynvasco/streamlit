import streamlit as st
import sympy as sp

def apply_term(equation, term):
    x = sp.symbols('x')
    if term.isnumeric():
        term_expr = sp.Rational(int(term))
    else:
        term_expr = sp.sympify(term)  # Parse the term as a symbolic expression
    equation_expr = sp.Eq(equation.lhs, equation.rhs)
    new_equation_expr = sp.Eq(equation_expr.lhs + term_expr, equation_expr.rhs + term_expr)
    new_equation = sp.simplify(new_equation_expr)
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
