import streamlit as st

def calculate_rule_of_three(value1, value2, value3):
    # Check if any value is zero to avoid division by zero
    if value1 == 0:
        return "Value 1 cannot be zero!"
    elif value2 == 0:
        return "Value 2 cannot be zero!"
    elif value3 == 0:
        return "Value 3 cannot be zero!"

    # Apply the rule of three
    result = (value2 * value3) / value1
    return result

def main():
    st.title("Rule of Three Game")

    st.write("Enter the values for the rule of three equation:")

    value1 = st.number_input("Value 1:", min_value=0.01, step=0.01)
    value2 = st.number_input("Value 2:", min_value=0.01, step=0.01)
    value3 = st.number_input("Value 3:", min_value=0.01, step=0.01)

    if st.button("Calculate"):
        result = calculate_rule_of_three(value1, value2, value3)
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()

