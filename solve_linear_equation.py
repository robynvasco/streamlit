import streamlit as st
from sympy import Symbol, Eq, simplify

def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    new_left_side = left_side + term
    new_right_side = right_side + term
    new_equation = Eq(new_left_side, new_right_side)
    return new_equation

def main():
    st.title("Equation Manipulator")

    equation = Eq((Symbol('x') + 3) / 15 + 3, 5)

    st.markdown("Original Equation:")
    st.latex(str(equation))

    term = st.text_input("Enter a term to apply to the equation (e.g., +1 or *2/3):")
    term = eval(term) if term else 0

    if st.button("Apply Term"):
        equation = apply_term_to_equation(term, equation)
        st.markdown("Updated Equation:")
        st.latex(str(equation))

if __name__ == "__main__":
    main()
