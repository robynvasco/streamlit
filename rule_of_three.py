import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.figure as mpl_fig

def plot_triangle(a, b, c):
    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    # Colors
    map_color = '#CCCCCC'
    a_color = '#336a91'
    b_color = '#0489c7'
    c_color = '#ed6478'
    x_color = '#ccdae3'

    # Plot triangle
    x = (b * c) / a
    fig = mpl_fig.Figure()
    ax = fig.add_subplot(111)
    ax.plot([0, a], [0, b], '-', color=map_color, solid_capstyle='round')
    ax.plot([0, c], [0, x], '-', color=map_color, solid_capstyle='round')
    ax.plot([0, a], [0, 0], '-', color=a_color, linewidth=3, label=f'Map Distance a = {a} cm', solid_capstyle='round')
    ax.plot([a, a], [0, b], '-', color=b_color, linewidth=3, label=f'Real Distance b = {b} km', solid_capstyle='round')
    ax.plot([0, c], [0, 0], '-', color=c_color, linewidth=5, label=f'Map Distance c = {c} cm', solid_capstyle='round')
    ax.plot([c, c], [0, x], '-', color=x_color, linewidth=3, label=f'Real Distance x', solid_capstyle='round')
    ax.plot([0, a], [0, 0], '-', color=a_color, linewidth=3, solid_capstyle='round')

    # Add labels
    ax.text(a/2, -0.7, "a", ha='center', va='bottom', color=a_color)
    ax.text(a-0.1, b/2, "b", ha='right', va='center', color=b_color)
    ax.text(c-0.5, -0.7, "c", ha='center', va='bottom', color=c_color)
    ax.text(c-0.1, x/2, "x", ha='right', va='center', color=x_color)
    
    # Set plot limits
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 16)
   
    
    # Hide axes and background
    ax.axis('off')
    ax.set_facecolor('none')
    
    # Show legend
    ax.legend(fontsize='x-small', loc='upper left')
    
    # Show plot
    st.pyplot(fig)

def main():
    st.title('Rule of Three')
    
    # Constants
    a = 2
    b = 3
    f=2/3
    # Calculate x
    x = lambda c: (b * c) / a
    
    st.info("If two centimeters on a map are equivalent to 3 km, then how far is the real distance between two points on the map that are 5 cm apart?")
    # User input for c
    c = st.slider('Map Distance c in cm', min_value=1, max_value=10, value=4)
    
    
    # Plot triangle
    plot_triangle(a, b, c)
    # Calculate distance
    distance = x(5)
    
    # Display formula in st.info
 
    st.info(f"a is to b as c is to x.\n\n"
            f"$\\frac{{a}}{{b}} = \\frac{{c}}{{x}}$\n")
    
    st.write("")
    answer = st.text_input("How far is the real distance between two points on the map that are 5 cm apart? Enter your answer for x (real distance in km):")
    if answer:
        try:
            if float(answer) == distance:
                st.success(f"That's correct! A distance of {c} cm on the map is equivalent to a real distance of x={distance} km")
            else:
                st.error("That's incorrect. Try again!")
        except ValueError:
            st.error("Invalid input. Please enter a number.")
           

    
    

if __name__ == '__main__':
    main()
