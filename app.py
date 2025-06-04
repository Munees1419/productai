import flipkart as fk
import welcome as wel
import login as lg
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def app():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated=False
    if "page" not in st.session_state:
        st.session_state.page="guest"
    

    if st.session_state.page=="guest":
        lg.login_page()
        if st.button("skip"):
            wel.welcome_page()
            
    
if __name__=="__main__":
    app()
