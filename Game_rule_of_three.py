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
            "answer": 12,
            "completed": False
        },
        {
            "scenario": "Water Conservation",
            "description": "Planet X-42 is facing a severe water shortage. Let's calculate how much water we need to save!",
            "values": (15, 3, 9),
            "answer": 45,
            "completed": False
        }
    ]

    level_index = 0
    while level_index < len(levels):
        level = levels[level_index]
        scenario = level["scenario"]
        description = level["description"]
        values = level["values"]
        answer = level["answer"]
        completed = level["completed"]

        st.header(f"Level {level_index + 1}: {scenario}")
        st.write(description)

        if not completed:
            # Input values
            st.subheader("Input Values:")
            a, b, c = values

            user_answer = st.number_input("How many days will it last?", value=0, min_value=0, key=f"answer_{level_index}")

            # Check answer
            if user_answer == answer:
                st.success("Congratulations! You provided the correct answer.")
                level["completed"] = True
            elif user_answer != 0:
                st.error("Oops! That's not the correct answer. Try again!")
                break

        level_index += 1

    if all(level["completed"] for level in levels):
        st.balloons()
        st.success("You saved Planet X-42! Well done!")

if __name__ == "__main__":
    main()
