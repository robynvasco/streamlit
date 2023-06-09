import streamlit as st
import random

def rule_of_three_calculator(a, b, c):
    # Calculate the unknown value using the Rule of Three
    x = (b * c) / a
    return x

def generate_scenario():
    # Generate random values for the scenario
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    # Calculate the unknown value using the Rule of Three
    x = rule_of_three_calculator(a, b, c)

    return a, b, c, x

def main():
    st.title("Rule of Three Adventure")

    st.write("Welcome to the Rule of Three Adventure! You find yourself in a mysterious land where everything revolves around proportions. Your mission is to solve the Rule of Three puzzles and find your way back home.")

    completed_levels = []
    while len(completed_levels) < 3:
        st.write("---")
        level = len(completed_levels) + 1
        st.write(f"Level {level}")

        if level not in completed_levels:
            st.write("You encounter a wise old wizard who presents you with a challenge:")

            # Generate a scenario
            a, b, c, x = generate_scenario()

            # Show the problem to the user
            st.write(f"Scenario: If {a} {get_object_plural(a)} cost {b} gold coins, how many gold coins would {c} {get_object_plural(c)} cost?")

            # Get user input for their answer
            user_answer = st.number_input("Enter your answer:", key=f"level_{level}", value=0, min_value=0, step=1)

            # Check if the user's answer is correct
            if user_answer == int(x):
                st.write("Correct! You have solved the puzzle.")
                completed_levels.append(level)
            else:
                st.write("Oops! That's not the correct answer. Try again!")

    st.write("---")
    st.write("Congratulations! You have successfully completed all levels and found your way back home.")

def get_object_plural(number):
    if number == 1:
        return "item"
    else:
        return "items"

if __name__ == "__main__":
    main()
