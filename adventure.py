import streamlit as st
import pyodbc

# Set up the database connection
def setup_database_connection():
    server = 'your_server_name'
    database = 'AdventureWorks'
    username = 'your_username'
    password = 'your_password'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    connection = pyodbc.connect(connection_string)
    return connection

# Execute SQL queries
def execute_sql_query(connection, sql_query):
    cursor = connection.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result

# Streamlit interface
def main():
    st.title("AdventureWorks Database Query")
    st.sidebar.header("User Query")
    user_query = st.sidebar.text_area("Enter your SQL query:")

    if st.sidebar.button("Run Query"):
        connection = setup_database_connection()
        result = execute_sql_query(connection, user_query)

        if result:
            st.write("Query Result:")
            st.write(result)
        else:
            st.write("No results found.")

if __name__ == "_main_":
    main()