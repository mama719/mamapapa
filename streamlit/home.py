import streamlit as st 
from pymongo import MongoClient 

def app():
    try:
          # change string to connection string 
        mongo_uri = "mongodb+srv://ciegalaxy2:123@cluster0.bvizeys.mongodb.net/"
        client = MongoClient(mongo_uri)

        # Selecting Database an collection to use
        db = client['task']
        collection = db["tasks"]

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
                st.write(id)
                collection.delete_one({"_id" : id})
                st.success("Delete made Successfull")

            result = collection.find()
            a = 0
            for res in result :
                if st.session_state["id"] == res["id"]:
                    a += 1
                    re = res["tasks"]
                    # st.markdown(f"<h1 style='background-color : grey ; border-radius : 30px ; margin:10px'><i style='background-color:blue ; border-radius:10px; padding-right:50px '>{a}.</i>{res["tasks"]}</h1>" , unsafe_allow_html=True)
                    st.header(f"{a}.{re}")
                    st.button("Delete Task" , id(a) , on_click=d , args=([res["_id"]]))
                        
    except:
        st.header("Something went wrong , Please check your internet and try again")

    

 
