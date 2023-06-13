import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex

def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    new_left_side = parse_expr("("+str(left_side)+")" + term)
    new_right_side = parse_expr("("+str(right_side)+")" + term)
    new_equation = Eq(new_left_side, new_right_side)
    return new_equation

def undo_last_action():
    if len(st.session_state['equations']) > 2:
        st.session_state['equations'] = st.session_state['equations'][:-2]
        st.write(st.session_state['equations'])

def main():
    st.title("Equation Manipulator")

    if 'equations' not in st.session_state:
        st.session_state['equations'] = [Eq((Symbol('x') + 3) / 15 + 3, 5)]
     
    st.info("Isolate x for the following equation")
    original_eq_container = st.container()

    # Create a column layout
    col1, col2, col3 = st.columns([3, 1, 1])

    term = col1.text_input(
        "b",
        label_visibility="collapsed",
        disabled=False,
        placeholder="e.g., +1 or *(1/2)",
    )
    term = str(term) if term else ""

    apply_clicked = False

    if col2.button("Apply Term"):
        apply_clicked = True

    if term and not apply_clicked:
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        st.session_state['equations'].append(equation)

    if len(st.session_state['equations']) > 2:
        if col3.button("Undo"):
            undo_last_action()
       

    # Display the updated equations
    with original_eq_container:
        equations = st.session_state['equations']
        for i, equation in enumerate(equations):
            st.latex(latex(equation))
            if i < len(equations) - 1:
                st.markdown("---")

if __name__ == "__main__":
    main()
