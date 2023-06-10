import streamlit as st

def calculate_unknown_value(a, b, c):
    # Applying the Rule of Three to calculate the unknown value
    unknown_value = (c * b) / a
    return unknown_value

def main():
    st.title("Galactic Explorer: The Rule of Three Adventure")
    st.write("Welcome, young space explorer! Your mathematical skills are crucial for our galactic mission.")

    levels = [
        {
            "scenario": "Oxygen Supply for the Space Station",
            "description": "Our space station is running low on oxygen reserves. We need to determine the optimal number of oxygen cylinders to sustain the crew.",
            "values": (20, 5, 50),
            "answer": 12,
            "completed": False
        },
        {
            "scenario": "Food Rations for Interstellar Journey",
            "description": "We are embarking on a long interstellar journey, and we need to calculate the amount of food rations required for the crew's sustenance.",
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

            st.write(f"a = {a}, b = {b}, c = {c}")

            user_answer = st.number_input("How many units are needed?", value=0, min_value=0, key=f"answer_{level_index}")

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
        st.success("Congratulations, Galactic Explorer! You have successfully completed all missions.")

if __name__ == "__main__":
    main()
