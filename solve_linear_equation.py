import streamlit as st
from sympy import Symbol, Eq, simplify, latex
from streamlit.legacy_caching.hashing import _CodeHasher


def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    new_left_side = left_side + term
    new_right_side = right_side + term
    new_equation = Eq(new_left_side, new_right_side)
    return new_equation

def main():
    st.title("Equation Manipulator")

    session_state = st.session_state.get(hash(_CodeHasher.hash("state")), {})
    if 'equation' not in session_state:
        session_state['equation'] = Eq((Symbol('x') + 3) / 15 + 3, 5)

    st.markdown("Original Equation:")
    st.latex(latex(session_state['equation']))

    term = st.text_input("Enter a term to apply to the equation (e.g., +1 or *2/3):")
    term = eval(term) if term else 0

    if st.button("Apply Term"):
        equation = apply_term_to_equation(term, session_state['equation'])
        session_state['equation'] = equation
        st.markdown("Updated Equation:")
        st.latex(latex(equation))

if __name__ == "__main__":
    main()
