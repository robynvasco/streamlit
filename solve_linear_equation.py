def main():
    st.title("Equation Manipulator")

    if 'equations' not in st.session_state:
        st.session_state['equations'] = [Eq((Symbol('x') + 3) / 15 + 3, 5)]
    if 'terms' not in st.session_state:
        st.session_state['terms'] = []

    st.info("Isolate x for the following equation")
    original_eq_container = st.container()

    # Create a column layout
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

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
        equation = apply_term_to_equation(term, st.session_state['equations'][-1])
        if equation != st.session_state['equations'][-1]:
            st.session_state['equations'].append(equation)
            st.session_state['terms'].append(term)

    if len(st.session_state['equations']) > 1:
        if col3.button("Undo"):
            undo_last_action()

    # Display the updated equations and terms
    with original_eq_container:
        equations = st.session_state['equations']
        terms = st.session_state['terms']
        for i, (equation, term) in enumerate(zip(equations, terms)):
            st.latex(latex(equation))
            col4.write(f"Term: {term}")
            if i < len(equations) - 1:
                st.markdown("---")
