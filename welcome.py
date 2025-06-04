import flipkart as fk
import login as lg
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
if 'messages'not in st.session_state:
    st.session_state.messages=[{"sender":"bot","text":"hello! how can I assist today?"}]

def add_message(sender,text):
    st.session_state.messages.append({"sender":sender,"text":text})

def welcome_page():
    st.sidebar.title("Home")
    login=st.sidebar.text("Login")
    st.sidebar.text("Logout")
    st.title("Product Chatbots")
    st.write("Ask your questions about our products")
    query=st.chat_input("Enter Product Name(e.g., mobile,tv)")
    if query:
        st.write(f"Searching for:{query}")
        data=fk.sflipkart(query)
        if data:
            df=pd.DataFrame(data)
            st.write("Product data")
            st.dataframe(df)
            csv=df.to_csv(index=False).encode("utf-8")
            st.download_button(label="Download CSV",data=csv,file_name=f"{query}filpkart.csv",mime="text/csv")
    else:
        st.warning("No data found")       
