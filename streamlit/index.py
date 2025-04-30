import streamlit as st 
from pymongo import MongoClient 

#Replace this with MongoDB connection string 
mongo_uri = "mongodb+srv://ciegalaxy2:123@cluster0.bvizeys.mongodb.net/"
client = MongoClient(mongo_uri)

#Select the database and collection you want to work with 
db = client["organization_database"]
collection = db["jobs"]

#streamlit app 
st.title("Mongo crud opreatoion With Streamlit")

#Create
st.header("Create Job")
create_title = st.text_input("Job Title" , key="create_title")
create_company = st.text_input("Company" , key="create_company")
create_location = st.text_input("Location" , key="create_location")
create_salary = st.number_input("Salary" , min_value=0 , key="create_salary" , format="%i" , step=10)

if st.button("Create Job") :
    job = {
        "title" : create_title ,
        "company" : create_company ,
        "location" : create_location ,
        "salary" : create_salary 
    }
    result = collection.insert_one(job)
    st.success(f"job created with id : {result.inserted_id}")

#Read 
st.header("Read Jobs")
if st.button("Read Jobs"):
    jobs = collection.find()
    for job in jobs :
        st.write(job)

#Update 
st.header("Update Job")
update_title = st.text_input("Title of the job to update" , key = "update_title")
new_company = st.text_input("New Company" , key = "new_company")
new_location = st.text_input("New Location" , key = "new Location")
new_salary = st.number_input("New Salary" , min_value=0 , key="new_salary" , format="%i")

if st.button("Update Job"):
    query = {"title" : update_title}
    update = {"$set" : {"company" : new_company , "location" : new_location , "salary" : new_salary}}
    result = collection.update_one(query , update)
    if result.match_count > 0 :
        st.success(f"Matched {result.matched.count} document(s) and modfied {result.modified_count}")
    else :
        st.warning("No Matching document found")

st.header("Delete Job")
delete_title = st.text_input("Title of the job to delete" , key="delete_title")

# Delete
if st.button("Delete Job"):
    query = {"title" : delete_title}
    result = collection.delete_one(query)
    if result.deleted_count > 0 :
        st.success(f"Deleted {result.deleted_count} document(s)")
    else:
        st.warning("No matching document found")

#close the connection when done 
client.close()
