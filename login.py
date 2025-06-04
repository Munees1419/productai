import streamlit as st
def login_page():
    st.title("login")
    user_id=st.text_input("user Id").upper()
    password=st.text_input("enter your password",type="password")
    if st.button("login"):
        if user_id and password:
            st.session_state.user_id=user_id
            if user_id:
                st.success("Login successful")

