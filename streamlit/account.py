import streamlit as st 
from pymongo import MongoClient 

def app():
    # change string to connection string 
    mongo_uri = "mongodb+srv://ciegalaxy2:123@cluster0.bvizeys.mongodb.net/"
    client = MongoClient(mongo_uri)

    # selecting database to use for project 
    db = client["user"]
    collection = db["users"]

    # initialize session
    if "id" not in st.session_state :
        st.session_state.id = ""
    if "first_name" not in st.session_state :
        st.session_state.first_name = ""
    if "last_name" not in st.session_state :
        st.session_state.first_name = "" 
    if "email" not in st.session_state :
        st.session_state.email = ""
    if "password" not in st.session_state:
        st.session_state.password = ""
    if "signedout" not in st.session_state :
        st.session_state.signedout = True
    if "signout" not in st.session_state :
        st.session_state.signout = False

    def l():
        while True :
            query = {"email" : email}
            result = collection.find_one(query)
            if bool(result) == False:
                st.warning("Wrong Email Address")
                break
            if password != result["password"]:
                st.warning("Something Went wrong please check your password and try again")
                break
            st.session_state.id = result["_id"]
            st.session_state.first_name = result["firstname"]
            st.session_state.last_name = result["lastname"]
            st.session_state.email = result['email']
            st.session_state.password = result['password']
            st.session_state.signedout = False
            st.session_state.signout = True
            st.success("User Logged In Successful")
            break

    def r() :
        st.session_state.signout = False 
        st.session_state.signedout = True
        st.session_state.id = ""
        st.session_state.first_name = ""
        st.session_state.last_name = ""
        st.session_state.email = ""
        st.session_state.password = ""

    if st.session_state["signedout"]:
        option = st.selectbox("Login / Signup" , ["Login" , "Signup"])

        if option == "Login":
            st.header("Welcome To Login Page")
            email = st.text_input("Email_Address")
            password = st.text_input("Password" , type="password")
            st.button("Login User" , on_click=l) 
                
    
        else :
            st.header("Welcome To Sign Up Page")
            col1 , col2 = st.columns(2)
            first_name = col1.text_input("First_Name")
            last_name = col2.text_input("Last_Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password" , type="password")
            if st.button("Create New User"):
                try:
                    if len(first_name) > 0 and len(last_name) > 0 and len(email) > 0 and len(password) > 0 :
                        record = {"firstname" : first_name , "lastname" : last_name , "email" : email , "password" : password}
                        query = {"email" : email}
                        result = collection.find_one(query)
                        if result :
                            error  = "Please , But User Already Exist"
                            st.warning(error)
                            st.write(result)
                        else:
                            data = collection.insert_one(record)
                            st.success("User Created Successfull")
                    else :
                        st.warning("Fill In All Feild , and Try Again")

                except: 
                        st.warning("Somethong Went Wrong Please Reload and Try Again")
    if st.session_state["signout"]:
        st.title("User Info:")
        st.header(f":green[First Name] : {st.session_state.first_name}")
        st.header(f":green[Last Name] : {st.session_state.last_name}")
        st.header(f":green[Email] : {st.session_state.email}")
        st.header(f":green[Password] : {st.session_state.password}")
        st.button("Log Out" , on_click=r) 