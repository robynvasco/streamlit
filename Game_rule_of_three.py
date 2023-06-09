import streamlit as st

def calculate_unknown_value(a, b, c):
    # Applying the Rule of Three to calculate the unknown value
    unknown_value = (c * b) / a
    return unknown_value

def main():
    st.title("Planet Saver: The Rule of Three Adventure")
    st.write("Welcome, young scientist! The fate of Planet X-42 depends on your mathematical skills.")

    levels = [
        {
            "scenario": "Oxygen Production",
            "description": "Planet X-42 is running out of oxygen, and we need to find the right proportions of resources to save it!",
            "values": (20, 5, 50),
            "answer": 12
        },
        {
            "scenario": "Water Conservation",
            "description": "Planet X-42 is facing a severe water shortage. Let's calculate how much water we need to save!",
            "values": (15, 3, 9),
            "answer": 45
        }
    ]

    level_index = st.sidebar.selectbox("Select a level:", range(len(levels)), format_func=lambda x: levels[x]["scenario"])

    level = levels[level_index]
    scenario = level["scenario"]
    description = level["description"]
    values = level["values"]
    answer = level["answer"]

    st.header(f"Level {level_index + 1}: {scenario}")
    st.write(description)

    # Input values
    st.subheader("Input Values:")
    a, b, c = values

    user_answer = st.number_input("How many days will it last?", value=0, min_value=0, key=f"answer_{level_index}")

    # Check answer
    if user_answer == answer:
        st.success("Congratulations! You provided the correct answer.")
        if level_index < len(levels) - 1:
            st.info("Prepare for the next level!")
        else:
            st.balloons()
            st.success("You saved Planet X-42! Well done!")

    elif user_answer != 0:
        st.error("Oops! That's not the correct answer. Try again!")

    # Display result
    st.subheader("Result:")
    st.write(f"With {c} oxygen tanks, it will last approximately {answer} days.")

if __name__ == "__main__":
    main()
