import streamlit as st

def rule_of_three_calculator(a, b, c):
    # Calculate the unknown value using the Rule of Three
    x = (b * c) / a
    return x

def main():
    st.title("Rule of Three Game")

    st.write("Welcome to the Rule of Three Game! In this game, you will practice using the Rule of Three to solve problems based on proportions.")

    st.write("Let's start with a simple example:")
    st.write("If 2 apples cost $3, how much would 5 apples cost?")

    # Get user input for the known values
    a = 2
    b = 3
    c = 5

    # Calculate the unknown value using the Rule of Three
    x = rule_of_three_calculator(a, b, c)


    # Get user input for their answer
    user_answer = st.number_input("Enter your answer:", value=0.0, step=0.01, format="%.2f")

    # Check if the user's answer is correct
    if abs(user_answer - x) < 0.01:
        st.write("Congratulations! Your answer is correct.")
    else:
        st.write(f"Oops! Your answer is incorrect. The correct answer is ${x}.")

    st.write("---")
    st.write("Let's try another example!")

    # Get user input for a new set of known values
    a = st.number_input("Enter the first number (a):", value=0.0, step=0.01, format="%.2f")
    b = st.number_input("Enter the second number (b):", value=0.0, step=0.01, format="%.2f")
    c = st.number_input("Enter the third number (c):", value=0.0, step=0.01, format="%.2f")

    # Calculate the unknown value using the Rule of Three
    x = rule_of_three_calculator(a, b, c)

    # Show the problem and the calculated unknown value
    st.write(f"The unknown value (x) is: {x}")

if __name__ == "__main__":
    main()
