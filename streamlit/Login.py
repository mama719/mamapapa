import streamlit as st 
import firebase_admin 
from firebase_admin import credentials , auth 

cred = credentials.Certificate("pondering-f2e35-5641dcd7b06f.json")
# firebase_admin.initialize_app(cred)

username = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password")

if st.button("Save") :
    user = auth.create_user(email = email , password = password , uid = username)

    st.success("Account created successfully")
    st.markdown("Please Login Using Your Email and Password ")
    st.balloons()
