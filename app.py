import streamlit as st
from db_utils import run_query, explain_query, create_index
from sample_queries import queries

st.title("🧠 SQL Performance Analyzer (PostgreSQL)")
st.write("Analyze execution time and query plans. Apply indexes to improve performance.")

selected_query = st.selectbox("🔍 Select a sample query", list(queries.keys()))
sql_query = queries[selected_query]

st.code(sql_query, language="sql")

if st.button("Run Query"):
    df, count = run_query(sql_query)
    st.success(f"Returned {count} rows.")
    st.dataframe(df)

if st.button("Show EXPLAIN ANALYZE Plan"):
    plan = explain_query(sql_query)
    st.code(plan)

if st.button("Apply Index on employee_id"):
    msg = create_index("employee_id")
    st.success(msg)
