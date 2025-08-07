import psycopg2
import pandas as pd
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    conn.close()
    return pd.DataFrame(rows, columns = col_names), len(rows)

def explain_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXPLAIN (ANALYZE, BUFFERS)" + query)
    plan = cursor.fetchall()
    conn.close()
    return "\n".join(row[0] for row in plan)

def create_index(column):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{column} ON employees({column})")
        conn.commit()
        return f"Index on {column}' created Successfully"
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()