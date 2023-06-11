import streamlit as st
import sympy as sp

def apply_term(equation, term):
    x = sp.symbols('x')
    new_equation = equation + term
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
