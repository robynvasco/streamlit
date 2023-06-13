import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex, SympifyError, sympify
import re
import random


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
        return new_equation
    except SympifyError:
        st.error("Invalid term. Please check the syntax and mismatched parentheses.")
        return equation


def undo_last_action():
        st.session_state['equations'] = st.session_state['equations'][:-1]
        st.session_state['terms'] = st.session_state['terms'][:-1]
        


def add_multiplication_operator(match):
    return match.group(1) + '*' + match.group(2)


def insert_multiplication_operators(term):
    term = re.sub(r'(\d)([a-zA-Z\(])', add_multiplication_operator, term)
    term = re.sub(r'(\))(?=[a-zA-Z])', add_multiplication_operator, term)
    return term


def start_new_game():
    equation_database = [
        Eq((Symbol('x') + 3) / 15 + 3, 5),
        Eq((Symbol('x') - 2) * 4 - 10, 6),
        Eq((Symbol('x') ** 2 + 5) / 2, 8),
        # Add more equations to the database
    ]
    random_equation = random.choice(equation_database)
    st.session_state['equations'] = [random_equation]
    st.session_state['terms'] = []


def main():
    st.title("Equation Manipulator")

    if 'equations' not in st.session_state:
        start_new_game()

    st.info("You can enter a term and apply it to both sides of the equation. Your aim is to isolate x to find a solution.")
    original_eq_container = st.container()
    st.write("")

    # Create a column layout
    col1, col2, col3 = st.columns([3, 1, 1])

    term = col1.text_input(
        "b",
        label_visibility="collapsed",
        placeholder="e.g., +1 or *(1/2)",
    )
    term = str(term) if term else ""

    apply_clicked = False
    undo_triggered = False

    if col2.button("Apply Term", key="apply"):
        apply_clicked = True
        
    if st.session_state['terms']:
        if col3.button("Undo", key="undo"):
            undo_triggered = True
            undo_last_action()

    if term and not apply_clicked and not undo_triggered:
        term = insert_multiplication_operators(term)
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        if equation != st.session_state['equations'][-1]:
            st.session_state['equations'].append(equation)
            st.session_state['terms'].append(term)

            # Check if x is isolated
            if equation.lhs == Symbol('x'):
                st.balloons()
                st.success("Congratulations! You have isolated x and found the solution!")
                st.button("Click here to begin a new game", key="new_game", on_click=start_new_game)

  

    # Display the updated equations and applied terms
    with original_eq_container:
        equations = st.session_state['equations']
        terms = st.session_state['terms']
        for i, equation in enumerate(equations):
            eq_col, term_col = st.columns([3, 1])
            with eq_col:
                st.latex(latex(equation))
                if i < len(equations) - 1:
                    st.markdown("---")
            with term_col:
                term = terms[i] if i < len(terms) else ''
                term_text = f"|    {term.replace('*', '⋅')}"
                st.latex(term_text)


if __name__ == "__main__":
    main()
