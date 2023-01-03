import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_ids, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    st.write(result)
    df = pd.DataFrame(result, columns=['User ID', 'Password ',  'City', 'Name', 'Phone','City_id'])
    with st.expander("Current Users"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_customer_ids()]
    selected_dealer = st.selectbox("User to Edit", list_of_dealers)
    selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        user_id = selected_result[0][0]
        password = selected_result[0][1]
        city = selected_result[0][2]
        name = selected_result[0][3]
        phone = selected_result[0][4]
        city_id = selected_result[0][5]

        # Layout of Create

        # col1, col2 = st.columns(2)
        # with col1:
        #     new_dealer_id = st.text_input("ID:", dealer_id)
        #     new_dealer_name = st.text_input("Name:", dealer_name)
        # with col2:
        #     new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])
        #     new_dealer_pin = st.text_input("Pin Code:", dealer_pin)
        # new_dealer_street = st.text_input("Street Name:", dealer_street)
    col1, col2 = st.columns(2)
    # with col1:
        # new_user_id = st.text_input("User ID:")
    new_user_id = user_id

    new_password = st.text_input("Password:")
        # new_city_id = st.text_input("City_id")
    new_city_id = city_id
    # with col2:
        # new_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai","Delhi"])
    new_city = city
        # new_name = st.text_input("Name:")
    new_name = name 
        # new_phone = st.text_input("Phone:")
    new_phone = phone 
    if st.button("Update Password"):
            edit_dealer_data(new_user_id, new_password, new_city, new_name, new_phone,new_city_id,user_id, password, city, name, phone,city_id)
            st.success("Successfully updated:: {} to ::{}".format(user_id, new_user_id))    

    result2 = view_all_data()
    # df2 = pd.DataFrame(result2, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    # with st.expander("Updated data"):
    #     st.dataframe(df2)
    df = pd.DataFrame(result, columns=['User ID', 'Password ',  'City', 'Name', 'Phone','City_id'])
    with st.expander("Current Users"):
        st.dataframe(df)
