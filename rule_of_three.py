import streamlit as st
import matplotlib.pyplot as plt

def calculate_real_distance(cm_on_map, cm_apart):
    km_on_map = 3
    real_distance = (cm_apart * km_on_map) / cm_on_map
    return real_distance

def plot_triangle():
    a = 3
    b = 2

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot([0, b], [a, a], 'k-')  # Draw the horizontal line
    ax.plot([b, b, 0], [0, a, a], 'k-')  # Draw the two vertical lines
    ax.set_xlim(-1, b + 1)
    ax.set_ylim(-1, a + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Display the plot
    st.pyplot(fig)

# Set the title of the app
st.title("Rule of Three")

# Display the question and gather user input
st.subheader("If two centimeters on a map is equivalent to 3 km,")
st.subheader("How far is the real distance of two points on the map that are 5 cm apart from each other?")
cm_on_map = st.number_input("Enter the number of centimeters on the map:", min_value=1)
cm_apart = st.number_input("Enter the distance between the two points on the map in centimeters:", min_value=1)

# Calculate the real distance and display the result
real_distance = calculate_real_distance(cm_on_map, cm_apart)
st.write("The real distance between the two points is", real_distance, "km.")

# Plot the triangle
st.subheader("Triangle Plot:")
plot_triangle()
