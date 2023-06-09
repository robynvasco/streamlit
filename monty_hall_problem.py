import random
import streamlit as st

def simulate_monty_hall(strategy):
    # Randomly place the car behind one of the three doors
    doors = ["goat"] * 3
    car_index = random.randint(0, 2)
    doors[car_index] = "car"

    # Player selects a door
    player_choice = random.randint(0, 2)

    # Monty opens a door with a goat
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] != "car"]
    monty_open = random.choice(remaining_doors)

    # Apply the selected strategy
    if strategy == "Stay":
        final_choice = player_choice
    elif strategy == "Switch":
        final_choice = [i for i in range(3) if i != player_choice and i != monty_open][0]
    else:
        remaining_doors_for_random_choice = [i for i in range(3) if i != monty_open]
        if remaining_doors_for_random_choice:
            final_choice = random.choice(remaining_doors_for_random_choice)
        else:
            final_choice = player_choice

    # Determine the result
    result = doors[final_choice]
    return result



def main():
    st.title("Monty Hall Problem Simulator")

    strategy = st.selectbox("Select a strategy", ("Stay", "Switch", "Random"))
    num_simulations = st.slider("Number of simulations", 100, 10000, 1000)

    st.write(f"**Strategy:** {strategy}")
    st.write(f"**Number of simulations:** {num_simulations}")

    wins = 0

    for _ in range(num_simulations):
        result = simulate_monty_hall(strategy)
        if result == "car":
            wins += 1

    st.write("### Results")
    st.write(f"{strategy}: {wins} wins out of {num_simulations} simulations")

if __name__ == "__main__":
    main()


