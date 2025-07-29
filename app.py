# login.py
import streamlit as st
from time import sleep

def check_credentials(username, password):
    # Replace with your actual authentication logic
    if username == "user" and password == "password":
        return True
    return False

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if check_credentials(username, password):
        st.session_state["logged_in"] = True
        st.success("Logged in successfully!")
        sleep(0.5) # Optional: add a small delay for user to see success message
        st.switch_page("main_app_page.py") # Replace with your target page
    else:
        st.error("Invalid username or password.")

# main_app_page.py
import streamlit as st

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("You need to log in to access this page.")
    st.switch_page("login.py") # Redirect to login if not logged in

st.title("Welcome to the Main App!")
st.write("This is the main content of your application.")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.success("Logged out!")
    sleep(0.5)
    st.switch_page("login.py")
