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

    while True:
        st.write("---")
        st.write("You encounter a wise old wizard who presents you with a challenge:")
        
        # Generate a scenario
        a, b, c, x = generate_scenario()

        # Show the problem to the user
        st.write(f"The wizard says, 'If {a} {get_object_plural(a)} cost {b} gold coins, how many gold coins would {c} {get_object_plural(c)} cost?'")
        
        # Get user input for their answer
        user_answer = st.number_input("Enter your answer:", key="wizard", value=0, min_value=0, step=1)

        # Check if the user's answer is correct
        if user_answer == int(x):
            st.write("The wizard smiles and says, 'Well done! You have solved the puzzle. You are one step closer to finding your way home.'")
        else:
            st.write("The wizard shakes his head and says, 'Oh no! That's not the correct answer. Try again!'")
            continue

        st.write("---")
        st.write("You continue on your journey and come across a group of merchants.")

        # Generate a scenario
        a, b, c, x = generate_scenario()

        # Show the problem to the user
        st.write(f"The merchants ask you, 'If {a} {get_object_plural(a)} cost {b} silver coins, how many silver coins would {c} {get_object_plural(c)} cost?'")

        # Get user input for their answer
        user_answer = st.number_input("Enter your answer:", key="merchants", value=0, min_value=0, step=1)

        # Check if the user's answer is correct
        if user_answer == int(x):
            st.write("The merchants nod in approval and say, 'Impressive! You have solved the puzzle. You are now closer to finding your way home.'")
        else:
            st.write("The merchants frown and say, 'That's not the correct answer. Please try again!'")
            continue

        st.write("---")
        st.write("As you journey further, you stumble upon a hidden treasure chest.")

        # Generate a scenario
        a, b, c, x = generate_scenario()

        # Show the problem to the user
        st.write(f"The treasure chest is locked with a secret code. The inscription reads, 'If {a} {get_object_plural(a)} cost {b} gems, how many gems would {c} {get_object_plural(c)} cost?'")

        # Get user input for their answer
        user_answer = st.number_input("Enter your answer:", key="treasure", value=0, min_value=0, step=1)

        # Check if the user's answer is correct
        if user_answer == int(x):
            st.write("The treasure chest opens with a click, revealing its valuable contents. Congratulations! You have solved the final puzzle and found your way back home.")
        else:
            st.write("The treasure chest remains locked. The secret code must be incorrect. Keep trying!")

        # Ask the user if they want to play again
        play_again = st.button("Play Again")
        if not play_again:
            break

def get_object_plural(number):
    if number == 1:
        return "item"
    else:
        return "items"

if __name__ == "__main__":
    main()
