from sqlalchemy import create_engine, text
import pandas as pd
from config import DB_CONFIG

# Create SQLAlchemy engine using pg8000
engine = create_engine(
    f"postgresql+pg8000://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

def run_query(query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df, len(df)

def explain_query(query):
    explain_sql = f"EXPLAIN (ANALYZE, BUFFERS) {query}"
    with engine.connect() as conn:
        result = conn.execute(text(explain_sql))
        plan_lines = [row[0] for row in result]
        return "\n".join(plan_lines)

def create_index(column):
    try:
        index_sql = f"CREATE INDEX IF NOT EXISTS idx_{column} ON employees({column})"
        with engine.connect() as conn:
            conn.execute(text(index_sql))
            return f"Index on '{column}' created successfully."
    except Exception as e:
        return f"Error: {e}"
