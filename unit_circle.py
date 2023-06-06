import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_unit_circle(alpha):
    x = np.cos(alpha)
    y = np.sin(alpha)

    plt.figure(figsize=(6, 6))
    plt.plot([0, x], [0, 0], 'g-', linewidth=2, label='cos')
    plt.plot([x, x], [0, y], 'r-', linewidth=2, label='sin')
    plt.plot([0, x], [0, y], 'b-', linewidth=2, label='Radius')
    plt.plot(x, y, 'bo', label='Point')
    plt.plot(np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)), 'gray', linestyle='--', alpha=0.3, label='Unit Circle')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Unit Circle: Sin and Cos')
    plt.legend()
    plt.grid(True)

    # Display the values of sin(alpha) and cos(alpha)
    st.markdown(f"<p style='text-align: center; font-size: 18px; margin-top: 20px;'>sin(alpha): {y:.4f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 18px;'>cos(alpha): {x:.4f}</p>", unsafe_allow_html=True)

    st.pyplot(plt)

def main():
    st.title('Unit Circle: Sin and Cos')
    
    with st.beta_container():
        col1, col2 = st.beta_columns(2)
        alpha = col1.slider('Select the angle (alpha)', 0.0, 2*np.pi, np.pi/4)
        plot_unit_circle(alpha)

        with col2.beta_expander("About"):
            st.markdown("This app visualizes the Unit Circle and shows the values of sin(alpha) and cos(alpha) for a selected angle (alpha).")
            st.markdown("Adjust the slider to change the angle and see the corresponding values on the circle.")
            st.markdown("The vectors for sin(alpha) and cos(alpha) are displayed on the x-axis and y-axis respectively.")
            
if __name__ == '__main__':
    main()


