import streamlit as st
from db import init_db as dbcon

##Design an application for learner to add gaurav training courses
st.title("Gaurav Training Course Selection")
#a variable to store courses selected by the user
selected_courses = []

#connect to database and fetch courses
@st.cache_resource #cache the connection to avoid reconnecting on every interaction
def get_db_connection():
    reuseconn = dbcon.main()
    dbcon.create_table_gaurav(reuseconn)
    training_courses_data = {
                            "UI5" : {"trainer": "Anubhav", "hours": 40, "price": 2000},
                            "python" : {"trainer": "Gaurav", "hours": 38, "price": 3000},
                            "CPI" : {"trainer": "Anubhav", "hours": 45, "price": 1000},
                            "CAPM" : {"trainer": "Gaurav", "hours": 48, "price": 4000},
                            "BTP" : {"trainer": "Saurabh", "hours": 48, "price": 5000},
                            "RAP" : {"trainer": "Gaurav", "hours": 54, "price": 6000},
                            }
    dbcon.execute_dml(reuseconn, training_courses_data)
    return reuseconn

myconn = get_db_connection() #establish connection and create table if not exists

#num = st.number_input("Enter a number")
#if st.button("Click me"):
#    if num > 5:
#        st.success(f"You entered a {num} greater than 5")
#    else:
#        st.error(f"👌You entered a {num} less than or equal to 5")    
