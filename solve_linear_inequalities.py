import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex, SympifyError, sympify, symbols, Rational, nsimplify, Float, Mul, S, And, Or, Not, Le, Lt, Ge, Gt, Eq, Ne
import re
import random

def enter():
    st.session_state.saved_input = st.session_state.input
    st.session_state.input = ''

def clear_text():
    st.session_state.input = ''

def apply_term(new_term, level, reverse_sign):
    term = insert_multiplication_operators(new_term)
    if reverse_sign:
        equation = apply_term_to_equation_reverse(term, st.session_state['equations'][-1])
    else:
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
    
    st.session_state['equations'].append(equation)
    st.session_state['terms'].append(term)

    # Check if x is isolated
    x_is_isolated = (equation.lhs == Symbol('x') and not equation.rhs.has(Symbol('x'))) or \
                    (equation.rhs == Symbol('x') and not equation.lhs.has(Symbol('x')))
    if x_is_isolated:
        st.success("Congratulations! 'x' is isolated and you have found the solution!")
        
            
            

def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    st.write("normal function is called")

    if "()" in term:
        st.error("Invalid term. Empty parentheses.")
        return equation

    try:
        new_left_side = sympify(f"({left_side}){term}")
        new_right_side = sympify(f"({right_side}){term}")
        if isinstance(equation, Eq):
            new_equation = Eq(new_left_side, new_right_side)
        elif isinstance(equation, Le):
            new_equation = Le(new_left_side, new_right_side)
        elif isinstance(equation, Ge):
            new_equation = Ge(new_left_side, new_right_side)
        elif isinstance(equation, Lt):
            new_equation = Lt(new_left_side, new_right_side)
        elif isinstance(equation, Gt):
            new_equation = Gt(new_left_side, new_right_side)
        else:
            st.error("Invalid equation type.")
        return new_equation
    except SympifyError:
        st.error("Invalid term. Please check the syntax and mismatched parentheses.")
        return equation

def apply_term_to_equation_reverse(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    st.write("Reverse function is called")

    if "()" in term:
        st.error("Invalid term. Empty parentheses.")
        return equation

    try:
        new_left_side = sympify(f"({left_side}){term}")
        new_right_side = sympify(f"({right_side}){term}")
        if isinstance(equation, Eq):
            new_equation = Eq(new_left_side, new_right_side)
        elif isinstance(equation, Le):
            new_equation = Ge(new_left_side, new_right_side)
        elif isinstance(equation, Ge):
            new_equation = Le(new_left_side, new_right_side)
        elif isinstance(equation, Lt):
            new_equation = Gt(new_left_side, new_right_side)
        elif isinstance(equation, Gt):
            new_equation = Lt(new_left_side, new_right_side)
        else:
            st.error("Invalid equation type.")
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
    # Replace ':' with '/' for division
    term = term.replace(':', '/')
    # Insert multiplication operators
    term = re.sub(r'(\d)([a-zA-Z\(])', add_multiplication_operator, term)
    term = re.sub(r'(\))(?=[a-zA-Z])', add_multiplication_operator, term)
    return term

def start_new_game(level):
    st.session_state.saved_input = ""
    equation_databases = {
        "Level 1": [
            Le(Symbol('x') + 3, 5),
            Le(Symbol('x') - 2, 4),
            Le(Symbol('x') * 2, 8),
        ],
        "Level 2": [
            Eq((Symbol('x') + 3) * 2, 5),
            Eq((Symbol('x') - 2) / 4, 6),
            Eq((Symbol('x') * 2) / 3, 8),
            Eq(Symbol('x') - 2/3, 8),
            Eq((Symbol('x') + 1) * 2, 10),
            Eq((Symbol('x') - 5) / 2, 3),
            Eq(((Symbol('x') * 3) / 4)+2, 9),
            Eq((Symbol('x') + 2) / 3, 5),
            Eq((Symbol('x') - 1) * 2, 8),
            Eq((Symbol('x') + 4) / 2, 6),
        ],
        "Level 3": [
            Eq(5/(Symbol('x') + 3), 5),
            Eq(1/Symbol('x') - 1/2 , 6),
            Eq(4/(Symbol('x') * 2), 8),
            Eq(1/Symbol('x') - 2/3, 8),
            Eq(4/(Symbol('x') + 1), 10),
            Eq(3/Symbol('x'), 3),
            Eq(8/(Symbol('x') * 3), 9),
            Eq(9/Symbol('x') + 2, 5),
            Eq(9/Symbol('x'), 3/2),
            Eq(1/(Symbol('x') + 4), 6),
        ],
        "Level 4": [
            Eq((Symbol('x') - 2) , 6* Symbol('x')),
            Eq(Symbol('x')+5, 6+2*Symbol('x')),
            Eq((Symbol('x') - 2), 2*Symbol('x')),
            Eq((Symbol('x') + 1), 3*Symbol('x')/2),
            Eq((Symbol('x') - 5), 3-Symbol('x')),
            Eq(Symbol('x'), 3-Symbol('x')),
            Eq((Symbol('x') * 3), (Symbol('x')/2 + 4)),
            Eq((Symbol('x') + 2) , Symbol('x') / 3),
            Eq((3*Symbol('x') - 1) , 1+2*Symbol('x')),
            Eq((Symbol('x') + 1) , 10*Symbol('x')),
            Eq((Symbol('x') - 5), 3+Symbol('x')/2),
            Eq((Symbol('x') * 3),Symbol('x') - 4),
            Eq((Symbol('x') + 2), Symbol('x') / 3),
        ],
         "Level 5": [
            Eq((Symbol('x') - 2) / Symbol('x'), 6),
            Eq((Symbol('x') - 1) / (Symbol('x')+3), 2),
            Eq(Symbol('x') / (Symbol('x')+3), 6),
            Eq(Symbol('x') / (Symbol('x')+5), 10),
            Eq(Symbol('x') / (Symbol('x')-2), 6),
            Eq(2 / Symbol('x')+5, 6/Symbol('x')),
            Eq(3 / (Symbol('x')+5), 3/Symbol('x')),
            Eq(1 / (Symbol('x')+2), 3/(Symbol('x')+7)),
            Eq(4 / (Symbol('x')+1), 3/(Symbol('x')+8)),
            Eq((Symbol('x') - 4) / 3 ,Symbol('x')+ 8),
            Eq((Symbol('x') + 1) * 2, 10*Symbol('x')),
            Eq((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Eq((Symbol('x') * 3), (Symbol('x') + 4)/3),
            Eq((Symbol('x') + 2) , Symbol('x') / 3+ 5),
            Eq((Symbol('x') - 1) * 2, (1+Symbol('x')) / 8),
            Eq((Symbol('x') + 4) / (2+Symbol('x')), 6),
            Eq((Symbol('x') - 2) / (2*Symbol('x')), 6),
            Eq((Symbol('x') + 1) * 2, (1+Symbol('x'))/2),
            Eq((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Eq((Symbol('x') * 3)+2, Symbol('x') / 4* 9),
            Eq((Symbol('x') + 2) + Symbol('x') / 3, 5+Symbol('x')),
        ]

        # Add more levels and equation databases
    }

    equation_database = equation_databases.get(level, [])

    random_equation = random.choice(equation_database)
    random_equation = replace_decimals_with_fractions(random_equation)
    st.session_state['equations'] = [random_equation]
    st.session_state['terms'] = []

def replace_decimals_with_fractions(equation):
    new_equation = equation
    x = Symbol('x')

    if equation.lhs.has(Float):
        new_lhs = nsimplify(equation.lhs)
        new_equation = Eq(new_lhs, equation.rhs)

    if equation.rhs.has(Float):
        new_rhs = nsimplify(equation.rhs)
        new_equation = Eq(equation.lhs, new_rhs)

    return new_equation



def main():
    st.title("Free x")

    if 'equations' not in st.session_state:
        start_new_game("Level 1")
        st.session_state.level="Level 1"

    st.info("You can enter a term and apply it to both sides of the equation. Your aim is to isolate x to find a solution.")
    original_eq_container = st.container()
    st.write("")

    # Create a column layout
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    level = st.sidebar.selectbox("Select Level", ["Level 1", "Level 2", "Level 3", "Level 4","Level 5"])  # Add more levels
    
    if st.session_state.level != level:
        start_new_game(level)
        st.session_state.level = level


    term = col1.text_input(
        "input",
        label_visibility="collapsed",
        value="",
        placeholder="e.g., +1 or *(1/2)",
        key="input",
        on_change=enter
    )
    

    undo = False
    apply = False
    st.session_state.reverse_sign= False

    if col2.button("Apply term", key="apply"):
        apply = True
    
    if col3.button("Apply term and reverse sign", key="reverse_apply"):
        apply = True
        st.session_state.reverse_sign = True

    if len(st.session_state['equations']) >=1:
        if col4.button("Undo", key="undo"):
            apply = True
            undo_last_action()

    if st.session_state.saved_input and not apply:
        apply_term(st.session_state.saved_input, level, st.session_state.reverse_sign)


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

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.button("Click here to begin a new game", key="new_game", on_click=lambda: start_new_game(level))

if __name__ == "__main__":
    main()
