import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input("User ID:")
        password = st.text_input("Password:")
        city_id = st.text_input("City_id")
    with col2:
        city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai","Delhi"])
        name = st.text_input("Name:")
        phone = st.text_input("Phone:")
    if st.button("Add User"):
        # print("hello1")
        add_data(user_id,password, city, name,phone, city_id)
        # print("hello3")
        st.success("Successfully added Dealer: {}".format(user_id))
