import streamlit as st
from sympy import Symbol, Eq, parse_expr, latex, SympifyError, sympify, simplify, symbols, Rational, nsimplify, Float, Mul, S, And, Or, Not, Le, Lt, Ge, Gt, Eq, Ne
import re
import random

def enter():
    st.session_state.saved_input = st.session_state.input
    st.session_state.input = ''

def clear_text():
    st.session_state.saved_input = ''

def apply_term(new_term, level, reverse_sign):
    term = insert_multiplication_operators(new_term)
    if reverse_sign:
        equation = apply_term_to_equation_reverse(term, st.session_state['equations'][-1])
    else:
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
    
    st.session_state['equations'].append(equation)
    st.session_state['terms'].append("|   $ "+term+"$")

    # Check if x is isolated
    x_is_isolated = (equation.lhs == Symbol('x') and not equation.rhs.has(Symbol('x'))) or \
                    (equation.rhs == Symbol('x') and not equation.lhs.has(Symbol('x')))
    if x_is_isolated:
        original_equation = st.session_state['equations'][0] 
        #Compare every equation in st.session_state.equations
        for i in range(1, len(st.session_state['equations'])):
            current_equation = st.session_state['equations'][i]
            # Simplify the current equation for comparison
            simplified_original = simplify(original_equation)
            simplified_current = simplify(current_equation)

            # Check if the current equation is different from the original equation
            if simplified_original != simplified_current:
                # Add a message to the equation indicating a mistake
                if i < len(st.session_state['terms']):
                    st.session_state['terms'][i] = ":orange[This inequality does not correspond to the original statement.]"
                    
                
            
        # Check if the last and the first equations are equal
        last_equation = st.session_state['equations'][-1]
        first_equation = st.session_state['equations'][0]
        simplified_last = simplify(last_equation)
        simplified_first = simplify(first_equation)

        if simplified_last == simplified_first:
            st.success("Congratulations! 'x' is isolated and you have found the solution!")
        else:
            st.error("Some of the inequalities do not correspond to the original statement. Make sure the inequality signs are correct.")
        
            
            

def apply_term_to_equation(term, equation):
    x = Symbol('x')
    left_side, right_side = equation.args
    

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
            Lt(Symbol('x') + 3, 5),
            Lt(Symbol('x') - 2, 4),
            Lt(Symbol('x') * 2, 8),
            Lt(Symbol('x') / 3, 2),
            Gt(Symbol('x') + 7, 10),
            Gt(Symbol('x') - 5, 1),
            Gt(Symbol('x') * 4, 12),
            Gt(Symbol('x') / 2, 3),
            Gt(Symbol('x') + 2, 6),
            Gt(Symbol('x') - 1, 3),
        ],
        "Level 2": [
            Lt((Symbol('x') + 3) * 2, 5),
            Lt((Symbol('x') - 2) / 4, 6),
            Le((Symbol('x') * 2) / 3, 8),
            Le(Symbol('x') - 2/3, 8),
            Le((Symbol('x') + 1) * 2, 10),
            Gt((Symbol('x') - 5) / 2, 3),
            Gt(((Symbol('x') * 3) / 4)+2, 9),
            Gt((Symbol('x') + 2) / 3, 5),
            Ge((Symbol('x') - 1) * 2, 8),
            Ge((Symbol('x') + 4) / 2, 6),
        ],
        "Level 3": [
            Lt(5/(Symbol('x') + 3), 5),
            Lt(-1/Symbol('x') - 1/2 , 6),
            Le(4/(Symbol('x') * (-2)), 8),
            Le(1/Symbol('x') - 2/3, 8),
            Ge(4/(Symbol('x') + 1), 10),
            Ge(3/Symbol('x'), 3),
            Gt(8/(Symbol('x') * (-3)), 9),
            Gt(-9/Symbol('x') + 2, 5),
            Gt(-9/Symbol('x'), 3/2),
            Lt(1/(Symbol('x') + 4), 6),
        ],
        "Level 4": [
            Lt((Symbol('x') - 2) , 6* Symbol('x')),
            Gt(Symbol('x')+5, 6+2*Symbol('x')),
            Lt((Symbol('x') - 2), 2*Symbol('x')),
            Gt((Symbol('x') + 1), 3*Symbol('x')/2),
            Ge((Symbol('x') - 5), 3-Symbol('x')),
            Ge(Symbol('x'), 3-Symbol('x')),
            Ge((Symbol('x') * 3), (Symbol('x')/2 + 4)),
            Gt((Symbol('x') + 2) , Symbol('x') / 3),
            Gt((3*Symbol('x') - 1) , 1+2*Symbol('x')),
            Le((Symbol('x') + 1) , 10*Symbol('x')),
            Le((Symbol('x') - 5), 3+Symbol('x')/2),
            Le((Symbol('x') * 3),Symbol('x') - 4),
            Lt((Symbol('x') + 2), Symbol('x') / 3),
        ],
         "Level 5": [
            Lt((Symbol('x') - 2) / Symbol('x'), 6),
            Lt((Symbol('x') - 1) / (Symbol('x')+3), 2),
            Lt(Symbol('x') / (Symbol('x')+3), 6),
            Le(Symbol('x') / (Symbol('x')+5), 10),
            Le(Symbol('x') / (Symbol('x')-2), 6),
            Le(2 / Symbol('x')+5, 6/Symbol('x')),
            Le(3 / (Symbol('x')+5), 3/Symbol('x')),
            Gt(1 / (Symbol('x')+2), 3/(Symbol('x')+7)),
            Gt(4 / (Symbol('x')+1), 3/(Symbol('x')+8)),
            Gt((Symbol('x') - 4) / 3 ,Symbol('x')+ 8),
            Ge((Symbol('x') + 1) * 2, 10*Symbol('x')),
            Ge((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Ge((Symbol('x') * 3), (Symbol('x') + 4)/3),
            Ge((Symbol('x') + 2) , Symbol('x') / 3+ 5),
            Lt((Symbol('x') - 1) * 2, (1+Symbol('x')) / 8),
            Le((Symbol('x') + 4) / (2+Symbol('x')), 6),
            Ge((Symbol('x') - 2) / (2*Symbol('x')), 6),
            Ge((Symbol('x') + 1) * 2, (1+Symbol('x'))/2),
            Lt((Symbol('x') - 5) / 2, 3+Symbol('x')),
            Le((Symbol('x') * 3)+2, Symbol('x') / 4* 9),
            Gt((Symbol('x') + 2) + Symbol('x') / 3, 5+Symbol('x')),
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
        apply_term(st.session_state.saved_input, level, st.session_state.reverse_sign)
    
    if col3.button("Apply term and reverse sign", key="reverse_apply"):
        apply = True
        st.session_state.reverse_sign = True
        apply_term(st.session_state.saved_input, level, st.session_state.reverse_sign)

    if len(st.session_state['equations']) >=1:
        if col4.button("Undo", key="undo"):
            apply = True
            undo_last_action()



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
                term_text = f"{term.replace('*', '⋅')}"
                st.markdown(term_text)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.button("Click here to begin a new game", key="new_game", on_click=lambda: start_new_game(level))
    clear_text()

if __name__ == "__main__":
    main()
