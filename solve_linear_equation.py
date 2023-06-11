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
    input_container = st.container()

    term = input_container.text_input("Enter a term to apply to the equation (e.g., +1 or *2/3):", key="term_input")
    term = str(term) if term else ""

    def apply_term_callback():
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        st.session_state['equations'].append(equation)

    input_container.text_input("Hidden Input", key="hidden_input", on_change=apply_term_callback, hidden=True)

    if input_container.button("Apply Term"):
        apply_term_callback()

    # Display the updated equations
    with original_eq_container:
        for equation in st.session_state['equations']:
            st.latex(latex(equation))
            st.markdown("---")

if __name__ == "__main__":
    main()
