import streamlit as st 
from pymongo import MongoClient 

def app() :
    try:
        if st.session_state.signout == False :
            st.title("Please Log In To Access This Page")
        else :
            # change string to connection string 
            mongourl = "mongodb+srv://ciegalaxy2:123@cluster0.bvizeys.mongodb.net/"
            client = MongoClient(mongourl)

            # select data base amd collection for work 
            db = client["user"]
            collection = db["users"]

            # update User Info
            with st.form("Update" , clear_on_submit=True):
                st.header("Update User Info : ")
                fn = st.text_input("First_Name")
                ln = st.text_input("Last_Name")
                e = st.text_input("Email")
                p = st.text_input("Password" , type="password")
                if st.form_submit_button("Update User Info" ) :
                    if len(fn) > 0 and len(ln) > 0 and len(e) > 0 and len(p) > 0 :
                        while True:
                            query1 = {"email" : e}
                            result1 = collection.find_one(query1)
                            
                            if result1 :
                                st.warning("User Already Exist ; Please Try Again")
                                break
                            query2 = {"_id" : st.session_state.id}
                            updata = {"$set" : {"firstname" : fn , "lastname" : ln , "email" : e , "password" : p}}
                            result2 = collection.find_one_and_update(query2 , updata)
                            result3 = collection.find_one(query1)
                            st.session_state.first_name = result3["firstname"]
                            st.session_state.last_name = result3["lastname"]
                            st.session_state.email = result3["email"]
                            st.session_state.password = result3["password"]
                            st.success("Update made successfully")
                            break  
                    else :
                        st.warning("Please fill in the field")
    except:
        st.warning("Please Check Your Internet Connection And Try Again")