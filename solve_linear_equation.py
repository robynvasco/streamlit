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
        "",
        label_visibility="collapsed",
        disabled=False,
        placeholder="e.g., +1 or *(1/2)",
    )
    term = str(term) if term else ""
    
    if term:
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        st.session_state['equations'].append(equation)
    
    if st.button("Apply Term"):
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        st.session_state['equations'].append(equation)
    
    if st.button("Go One Step Back"):
        if len(st.session_state['equations']) > 1:
            st.session_state['equations'].pop()
    
    # Display the updated equations
    with original_eq_container:
        for equation in st.session_state['equations']:
            st.latex(latex(equation))
            st.markdown("---")

if __name__ == "__main__":
    main()
