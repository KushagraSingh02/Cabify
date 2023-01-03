# Importing pakages
import streamlit as st
# import mysql.connector
import base64
from create import create
from database import create_table
from delete import delete
from read import read 
from update import update
from execute import execute
from streamlit_option_menu import option_menu as om
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()
#
# c.execute("CREATE DATABASE ebike")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
   


def main():
#     st.markdown(
#     f"""

#         <style>
#          .stApp {{
#              background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#    """,
#    unsafe_allow_html=True)
    add_bg_from_local('cab.jpg')

    # st.title("Smooth Rides")
    # menu = ["Add", "View", "Edit", "Remove","Execute"]
    # choice = st.sidebar.selectbox("Menu", menu)
    choice = om(None, ["Add", "View", "Edit", "Remove","Execute"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    # selected2

    # create_table()
    if choice == "Add":
        st.subheader("Enter User Details:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()
    elif choice == "Execute":
        st.subheader("Execute the Query")
        execute()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
