# streamlit_app.py
import streamlit as st

def main():
    st.title("My Streamlit App")
    
    # Add a sidebar
    st.sidebar.header("Options")
    option = st.sidebar.selectbox("Select an option", ["Home", "About", "Contact"])

    # Display content based on the selected option
    if option == "Home":
        st.write("Welcome to the Home page!")
    elif option == "About":
        st.write("This is the About page. Streamlit is a great tool for creating web apps!")
    elif option == "Contact":
        st.write("Contact us at contact@example.com")

if __name__ == "__main__":
    main()
