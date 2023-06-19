import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex, SympifyError, sympify, symbols
import re

def enter():
    st.session_state.saved_input = st.session_state.input
    st.session_state.input = ''

def clear_text():
    st.session_state.input = ''

def apply_term(new_term, level):
    term = insert_multiplication_operators(new_term)
    equation = apply_term_to_equation(term, st.session_state['equations'][-1])
    if equation != st.session_state['equations'][-1]:
        st.session_state['equations'].append(equation)
        st.session_state['terms'].append(term)

        # Check if x is isolated
        if equation.lhs == Symbol('x') and symbols('x') not in equation.rhs.free_symbols:
            st.balloons()
            st.success("Congratulations! You have isolated x and found the solution!")
            st.button("Click here to begin a new game", key="new_game", on_click=lambda: start_new_game(level))

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
    if len(st.session_state['equations']) > 1:
        st.session_state['equations'] = st.session_state['equations'][:-1]
        st.session_state['terms'] = st.session_state['terms'][:-1]

def add_multiplication_operator(match):
    return match.group(1) + '*' + match.group(2)

def insert_multiplication_operators(term):
    term = re.sub(r'(\d)([a-zA-Z\(])', add_multiplication_operator, term)
    term = re.sub(r'(\))(?=[a-zA-Z])', add_multiplication_operator, term)
    return term

def start_new_game(level):
    st.session_state.saved_input = ""
    equation_databases = {
        "Level 1": [
            Eq(Symbol('x') + 3, 5),
            Eq(Symbol('x') - 2, 4),
            Eq(Symbol('x') * 2, 8),
            Eq(Symbol('x') / 3, 2),
            Eq(Symbol('x') + 7, 10),
            Eq(Symbol('x') - 5, 1),
            Eq(Symbol('x') * 4, 12),
            Eq(Symbol('x') / 2, 3),
            Eq(Symbol('x') + 2, 6),
            Eq(Symbol('x') - 1, 3),
        ],
        "Level 2": [
            Eq((Symbol('x') + 3) * 2, 5),
            Eq((Symbol('x') - 2) / 4, 6),
            Eq((Symbol('x') * 2) / 3, 8),
            Eq(Symbol('x') - 2/3, 8),
            Eq((Symbol('x') + 1) * 2, 10),
            Eq((Symbol('x') - 5) / 2, 3),
            Eq((Symbol('x') * 3) / 4+2, 9),
            Eq((Symbol('x') + 2) / 3, 5),
            Eq((Symbol('x') - 1) * 2, 8),
            Eq((Symbol('x') + 4) / 2, 6),
        ],
        "Level 3": [
            Eq(2 / Symbol('x'), 6),
            Eq(2 / (3 +Symbol('x')), 8),
            Eq((Symbol('x') + 1) * 2, 10*Symbol('x')),
            Eq((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Eq((Symbol('x') * 3)+Symbol('x') / 4, 9),
            Eq((Symbol('x') + 2) + Symbol('x') / 3, 5),
            Eq((Symbol('x') - 1) * 2, 8),
            Eq((Symbol('x') + 4) / (2+Symbol('x')), 6),
        ],
         "Level 4": [
            Eq((Symbol('x') - 2) / Symbol('x'), 6),
            Eq((Symbol('x') - 2) / 3 *Symbol('x'), 8),
            Eq((Symbol('x') + 1) * 2, 10*Symbol('x')),
            Eq((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Eq((Symbol('x') * 3)+Symbol('x') / 4, 9),
            Eq((Symbol('x') + 2) + Symbol('x') / 3, 5),
            Eq((Symbol('x') - 1) * 2, 8),
            Eq((Symbol('x') + 4) / (2+Symbol('x')), 6),
        ]
        # Add more levels and equation databases
    }

    equation_database = equation_databases.get(level, [])
    st.session_state['equations'] = equation_database
    st.session_state['terms'] = []

def main():
    st.title("Free x")

    if 'equations' not in st.session_state:
        start_new_game("Level 1")
        st.session_state.level = "Level 1"
        st.session_state.equation_index = 0

    st.info("You can enter a term and apply it to both sides of the equation. Your aim is to isolate x to find a solution.")
    original_eq_container = st.container()
    st.write("")

    # Create a column layout
    col1, col2, col3 = st.columns([3, 1, 1])

    level = st.sidebar.selectbox("Select Level", ["Level 1", "Level 2", "Level 3", "Level 4"])  # Add more levels
    
    if st.session_state.level != level:
        start_new_game(level)
        st.session_state.level = level

    term = col1.text_input(
        "Input",
        label_visibility="collapsed",
        value="",
        placeholder="e.g., +1 or *(1/2)",
        key="input",
        on_change=enter
    )

    undo = False
    apply = False

    if col2.button("Apply term", key="apply"):
        apply = True

    if len(st.session_state['equations']) >= 1:
        if col3.button("Undo", key="undo"):
            apply = True
            undo_last_action()

    if st.session_state.saved_input and not apply:
        apply_term(st.session_state.saved_input, level)

    # Display the updated equations and applied terms
    with original_eq_container:
        equations = st.session_state['equations']
        terms = st.session_state['terms']
        equation_index = st.session_state.get('equation_index', 0)
        if equation_index < 0:
            equation_index = 0
        elif equation_index >= len(equations):
            equation_index = len(equations) - 1
        st.session_state.equation_index = equation_index
        equation = equations[equation_index]

        equation_row = st.row()
        equation_row.latex(latex(equation))

        term_row = st.row()
        term = terms[equation_index] if equation_index < len(terms) else ''
        term_text = f"|    {term.replace('*', '⋅')}"
        term_row.latex(term_text)

        prev_button, next_button = st.columns(2)
        if prev_button.button("Previous Equation") and equation_index > 0:
            st.session_state.equation_index -= 1
        if next_button.button("Next Equation") and equation_index < len(equations) - 1:
            st.session_state.equation_index += 1

if __name__ == "__main__":
    main()
