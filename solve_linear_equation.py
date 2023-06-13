import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex, SympifyError, sympify
import re



def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
   
    if "()" in term:
        st.error("Invalid term. Empty parentheses.")
        return equation
      
    try:
        new_left_side = sympify(f"({left_side}){term}")
        new_right_side = sympify(f"({right_side}){term}")
        new_equation = Eq(new_left_side, new_right_side)
        new_left_side_raw = parse_expr(f"({left_side}){term}", evaluate=False)
        new_right_side_raw = parse_expr(f"({right_side}){term}", evaluate=False)
        unsimplified_equation = Eq(new_left_side_raw, new_right_side_raw)
            
        return unsimplified_equation, new_equation
    except SympifyError:
        st.error("Invalid term. Please check the syntax and mismatched parantheses.")
        return equation



def undo_last_action():
    if len(st.session_state['equations']) > 2:
        st.session_state['equations'] = st.session_state['equations'][:-2]
        st.write(st.session_state['equations'])

def add_multiplication_operator(match):
    return match.group(1) + '*' + match.group(2)

def insert_multiplication_operators(term):
    term = re.sub(r'(\d)([a-zA-Z\(])', add_multiplication_operator, term)
    term = re.sub(r'(\))(?=[a-zA-Z])', add_multiplication_operator, term)
    return term

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
        term = insert_multiplication_operators(term)
        equations = apply_term_to_equation(term, st.session_state['equations'][-1])
        for equation in equations:
            if equation != st.session_state['equations'][-1]:
                st.session_state['equations'].append(equation)

    if len(st.session_state['equations']) > 1:
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
