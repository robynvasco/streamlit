import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex

def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    new_left_side = parse_expr("("+str(left_side)+")" + term)
    new_right_side = parse_expr("("+str(right_side)+")" + term)
    new_equation = Eq(new_left_side, new_right_side)
    return new_equation

def main():
    st.title("Equation Manipulator")

    if 'equation' not in st.session_state:
        st.session_state['equation'] = Eq((Symbol('x') + 3) / 15 + 3, 5)

    original_eq_container = st.container()
    updated_eq_container = st.container()

    with original_eq_container:
        st.markdown("Original Equation:")
        st.latex(latex(st.session_state['equation']))

    st.write("Enter a term to apply to the equation (e.g., +1 to add one or *2/3 to multiply with 2/3):")
    col1, col2 = st.columns(2)

    with col1:
        term = st.text_input()
    with col2:
        st.button("Apply Term", on_click=apply_term)

    with updated_eq_container:
        st.markdown("Updated Equation:")
        st.latex(latex(st.session_state['equation']))

def apply_term():
    equation = apply_term_to_equation(term, st.session_state['equation'])
    st.session_state['equation'] = equation

if __name__ == "__main__":
    main()
