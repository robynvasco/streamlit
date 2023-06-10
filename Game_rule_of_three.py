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
            "scenario": "Oxygen Rescue Mission",
            "description": "Our spacecraft has crash-landed on an alien planet. To survive, we need to calculate how many oxygen cylinders are needed for a 10-day expedition. Each cylinder provides enough oxygen for 2 days. The remaining oxygen cylinders are 8. Calculate the unknown value.",
            "answer": 20,
            "completed": False
        },
        {
            "scenario": "Power Generation for Warp Engine",
            "description": "We're stranded in deep space without power! We must calculate the amount of energy cells required to activate the warp engine for a hyperspace jump. Each cell powers the engine for 3 hours, and the journey will take 12 hours. Calculate the unknown value, the total number of energy cells needed.",
            "answer": 4,
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

        if level_index == 0 or levels[level_index - 1]["completed"]:
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
        else:
            break

        level_index += 1

    if all(level["completed"] for level in levels):
        st.balloons()
        st.success("Congratulations, Galactic Explorer! You have successfully completed all missions.")

if __name__ == "__main__":
    main()
