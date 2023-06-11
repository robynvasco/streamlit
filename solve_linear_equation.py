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

    if 'equations' not in st.session_state:
        st.session_state['equations'] = [Eq((Symbol('x') + 3) / 15 + 3, 5)]
     
    st.info("Isolate x for the following equation")
    original_eq_container = st.container()
    

    term = st.text_input(
        label_visibility="collapsed",
        disabled=False,
        placeholder="eg. +1 or *(1/2)",
    )
    term = str(term) if term else ""

    if st.button("Apply Term"):
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        st.session_state['equations'].append(equation)
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    
    # Display the updated equations
    with original_eq_container:

        for equation in st.session_state['equations']:
            st.latex(latex(equation))
            st.markdown("---")

if __name__ == "__main__":
    main()
