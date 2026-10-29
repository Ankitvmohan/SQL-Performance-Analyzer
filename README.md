## **SQL PERFORMANCE ANALYZER**

An Interactive PostgreSQL Dashboard for exploring SQL query execution, analyzing execution plans, and experimenting with indexing using Python and Streamlit.

[🚀 <u> **Click here to launch the app** </u>](https://sql-performance-analyzer-001.streamlit.app/)

[📸 Snapshots](https://github.com/Ankitvmohan/SQL-Performance-Analyzer/tree/main/Snapshot)

## 📌 **Overview**

Writing a SQL query that returns the correct result is only a part of working with databases.

Understanding how a DBMS executes any query can help us identify opportunities to improve performance.

This interactive dashboard is built to explore SQL query execution and basic database optimization concepts using an employee dataset that is stored in PostgreSQL.

Users can run predefined queries, inspect the returned records, view execution plans, and create indexes to experiment with index-based filtering.

The project connects Python and PostgreSQL and presents database operations through a simple Streamlit Interface.

---
## 🎯 **Impact of the Project**
This project demonstrates the practical application of SQL, Python, and Relational database concepts through an interactive tool.

- <u>*SQL query Analysis:*</u> Explores the entire table, range filtering, exact-match filtering, and aggregation.
- <u>*Execution-plan analysis:*</u> Inspect the PostgreSQL execution plans with EXPLAIN (ANALYZE, BUFFERS).
- <u>*Indexing Concepts:*</u> Create an index and investigate how indexes may affect filtering queries.
- <u>*Database Integration:*</u> Connect a Python application to PostgreSQL and retrieve query results.
- <u>*Interactive Data Presentation:*</u> Display returned records and row counts through Streamlit and Pandas.

This application provides a practical way to explore query behaviour.

---
## ⚙️ **How Does it Work?**
The application follows a simple workflow:

1. Select a sample query from the dashboard's dropdown menu.
2. Inspect the selected query before execution for any errors and the one you are looking for.
3. Execute it against the PostgreSQL database by running the query.
4. Check the returned row count and the query results in a dataframe by viewing the output.
5. Select the Show EXPLAIN ANALYZE button to inspect the execution plan output, which provides the timestamp of planning and execution time.
6. Create an index on the employee_id and examine its potential effect on relevant filtering queries.
---

## 📄 **Technology Stack**
- Python
- SQL
- PostgreSQL
- Streamlit
- Pandas
- Psycopg2
- Git and GitHub
- Streamlit Cloud

---

## 📈 **Room for Improvements**
The project establishes a foundational understanding of SQL execution-plan analysis. The following improvements could make it more useful as a database performance tool.

1. *Reliable Performance Benchmarking:* Run queries multiple times and report median or average execution time. Including the caching and other factors for better performance comparisons.

2. *More Indexing Experiments:* Can explore composite indexes, different filtering conditions, and queries involving sorting or multiple columns.

3. *Better Error Handling:* Improve the handling of invalid SQL statements, missing tables, and index-creation errors by ensuring safe management of database connections and transactions.
