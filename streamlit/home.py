import streamlit as st 
from pymongo import MongoClient 

def app():

    # change string to connection string 
    mongo_uri = "mongodb+srv://ciegalaxy2:123@cluster0.bvizeys.mongodb.net/"
    client = MongoClient(mongo_uri)

    # Selecting Database an collection to use
    db = client['task']
    collection = db["tasks"]

    if "up" not in st.session_state :
        st.session_state.up = False
    if "uid" not in st.session_state :
        st.session_state.uid = ""

    def up(task):
        query = {"_id" : st.session_state.uid}
        result = {"$set" : {"tasks" : task}}
        collection.find_one_and_update(query , result)
        st.session_state.up = False
        pass

    if st.session_state.up :
        task = st.text_area(":orange[Update_New_Task]" , placeholder = "Enter Your Task To Be Updated")
        st.button("Save Data" , on_click = up , args=[(task)])
    else :

        if st.session_state.signedout :
            st.title("Please Login To Access Your Data")
        else :
            st.title("Welcome To Home Page")
            task = st.text_area(":orange[+ New Task]" , placeholder="Add New Task Here")
            if st.button("Add Task") :
                if len(task) > 0:
                    job = {"tasks" : task , "id" : st.session_state.id}
                    data = collection.insert_one(job)
                    st.success("Task Added Successfully")
                else :
                    st.warning('Your Text Area is Blank')

            def d(id):
                collection.delete_one({"_id" : id})
                st.success("Delete made Successfull")
            
            def u(id):
                st.session_state.uid = id
                st.session_state.up = True

            result = collection.find()
            a = 0
            for res in result :
                if st.session_state["id"] == res["id"]:
                        with st.container(border=True):
                            a += 1
                            st.header(f"Task_NO.{a}")
                            st.subheader(f"{res['tasks']}")
                            col1 , col2 = st.columns(2)
                            col1.button("Delete Task" , id(a) , on_click=d , args=([res["_id"]]) )
                            col2.button("Update Task" , id(a + 100) , on_click=u , args=([res["_id"]]) ) 
                            

                    




