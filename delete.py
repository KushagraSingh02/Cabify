import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_ids, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['User ID', 'Password ',  'City', 'Name', 'Phone','City_id'])
    with st.expander("Current Users"):
        st.dataframe(df)

    list_of_users = [i[0] for i in view_only_customer_ids()]
    selected_user = st.selectbox("Task to Delete", list_of_users)
    st.warning("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete User"):
        delete_data(selected_user)
        st.success("Dealer has been deleted successfully")
    new_result = view_all_data()
    df = pd.DataFrame(result, columns=['User ID', 'Password ',  'City', 'Name', 'Phone','City_id'])
    with st.expander("Current Users"):
        st.dataframe(df)