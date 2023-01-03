import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    # df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    # with st.expander("View all Dealers"):
    #     st.dataframe(df)
    df = pd.DataFrame(result, columns=['User ID', 'Password ',  'City', 'Name', 'Phone','City_id'])
    with st.expander("Current Users"):
        st.dataframe(df)
    with st.expander("User Location"):
        task_df = df['City'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='City')
        st.plotly_chart(p1)