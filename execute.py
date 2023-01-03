import mysql.connector
import datetime

import pandas as pd
import streamlit as st

# import mariadb
    
# mydb =  mariadb.connect(
#   host="localhost",
#   user="root",
# #   password="%T5687j5IiYe"
#     database="ebike"
# )
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="cs657_project"
)
c = mydb.cursor()

def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 

def execute():
    
    # col1,col2 = st.columns(2)

    # with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("SQL Code Here")
            submit_code = st.form_submit_button("Execute")

        #Table containg info

        # with st.expander("Table Info"):
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)
                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)
                    
                with st.expander("Tabular Format"):
                    # query_df = pd.dataFrame(,)
                    query_df = pd.DataFrame(query_results,columns=[i[0] for i in c.description])
                    st.dataframe(query_df)

			
				
