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
            "description": "As a brave explorer, you have landed on an alien planet called Zephyria. Your mission is to rescue a team of stranded astronauts. Upon arrival, the alien inhabitants provided you with a map of the planet's surface. According to the map, 5 centimeters represent 600 meters in reality. The location of the astronauts' base camp is marked 8 centimeters away from your landing site on the map. How far, in meters, is the base camp from your landing site?",
            "answer": 960,
            "completed": False
        },
        {
            "scenario": "Cargo Transport Mission",
            "description": "In a nearby star system, there is a bustling trade between planets. Yesterday, 2 cargo ships transported goods from a distant planet to the spaceport. Today, 3 cargo ships of the same size as yesterday, made 6 trips to transport the same amount of goods from the spaceport to the intergalactic mall. How many trips did each cargo ship make yesterday?",
            "answer": 9,
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
