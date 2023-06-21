import streamlit as st
import matplotlib.pyplot as plt

def draw_square(a, b):
    fig, ax = plt.subplots()
    ax.plot([0, a, a, 0, 0], [0, 0, b, b, 0], 'b-')
    ax.set_xlim([0, a])
    ax.set_ylim([0, b])
    ax.set_aspect('equal')
    plt.axis('off')
    return fig

def main():
    st.title("Square Visualization")
    st.write("Enter the dimensions of the square:")
    a = st.number_input("Side A:", value=1, step=1)
    b = st.number_input("Side B:", value=1, step=1)
    
    if st.button("Draw Square"):
        fig = draw_square(a, b)
        st.pyplot(fig)

if __name__ == "__main__":
    main()

