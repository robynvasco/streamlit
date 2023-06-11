import streamlit as st
import re

def apply_term(equation, term):
    equation_parts = re.split(r'(\+|\-|\*|/)', equation)
    new_parts = []

    for part in equation_parts:
        if part.strip() == '':
            continue

        if part.isnumeric():
            new_parts.append(str(eval(part + term)))
        else:
            new_parts.append(part)

    return ''.join(new_parts)

def main():
    st.title("Equation App")
    equation = "(x+3)/15+3=5"
    st.write("Current equation:", equation)

    term = st.text_input("Enter a term to apply to the equation (e.g., +1, *2/3)")

    if st.button("Apply Term"):
        new_equation = apply_term(equation, term)
        st.write("Updated equation:", new_equation)
        equation = new_equation

if __name__ == "__main__":
    main()
