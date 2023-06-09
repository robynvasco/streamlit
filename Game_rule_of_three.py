import streamlit as st

def calculate_unknown_value(a, b, c):
    # Applying the Rule of Three to calculate the unknown value
    unknown_value = (c * b) / a
    return unknown_value

def main():
    st.title("Planet Saver: The Rule of Three Adventure")
    st.write("Welcome, young scientist! The fate of Planet X-42 depends on your mathematical skills.")

    # Example scenario
    st.header("Scenario: Oxygen Production")
    st.write("Planet X-42 is running out of oxygen, and we need to find the right proportions of resources to save it!")
    st.write("We have 20 oxygen tanks that last for 5 days. How many days will 50 oxygen tanks last?")

    # Input values
    st.subheader("Input Values:")
    a = st.number_input("Number of oxygen tanks (1st value)", value=20)
    b = st.number_input("Number of days (1st value)", value=5)
    c = st.number_input("Number of oxygen tanks (2nd value)", value=50)

    # Calculate unknown value
    unknown_value = calculate_unknown_value(a, b, c)

    # Display result
    st.subheader("Result:")
    st.write(f"With {c} oxygen tanks, it will last approximately {unknown_value} days.")

if __name__ == "__main__":
    main()
