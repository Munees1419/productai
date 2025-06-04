import google.generativeai as gen
import streamlit as st
gen.configure(api_key='AIzaSyBebu9JXr_Ek0uruCAuFXWs-v5dbDKmNao')
model=gen.GenerativeModel('gemini-2.0-flash')

def get_gemini_response(combined_prompt):
    response=model.generate_content(combined_prompt)
    query=response.text
    return query
