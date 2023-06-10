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
            "description": "Our space station is running low on oxygen reserves. To sustain the crew for 50 days, we need to determine how many oxygen cylinders (a) are needed if each cylinder lasts for 5 days (b). The current number of oxygen cylinders available (c) is 20. Calculate the unknown value.",
            "answer": 12,
            "completed": False
        },
        {
            "scenario": "Food Rations for Interstellar Journey",
            "description": "We are embarking on a long interstellar journey, and we need to calculate the amount of food rations required for the crew's sustenance. Each crew member requires 3 rations per day (b). The journey will last for 9 days, and we have 15 crew members on board. Calculate the unknown value (a), the total number of food rations needed (c).",
            "answer": 45,
            "completed": False
        }
    ]

    level_index = 0
    while level_index < len(levels):
        level = levels[level_index]
        scenario = level["scenario"]
        description = level["description"]
        answer = level["answer"]
        completed = level["completed"]

        st.header(f"Level {level_index + 1}: {scenario}")
        st.write(description)

        if not completed:
            user_answer = st.number_input("Enter your answer:", value=0, min_value=0, key=f"answer_{level_index}")

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
