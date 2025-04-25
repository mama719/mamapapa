import streamlit as st 
from streamlit_option_menu import option_menu 
import home , account

st.title(":blue[Proper record Tracker : ] :green[Todo's]")

st.markdown("---")

with st.sidebar :
    app = option_menu(
    menu_title = "Todo's" ,
    menu_icon = ["table"] ,
    options = ["Home" , "Account"] ,
    icons = ["house-fill" , 'person-circle'] ,
    default_index = 1 ,
    styles = {
        "icon" : {"font-size" : "23px"} ,
        "nav-link" : {"font-size" : "20px"},
        "nav-link-selected" : {"background-color" : "blue"}
    }),

if "Home" in app :
    home.app()
if "Account"in app :
    account.app()
