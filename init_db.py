import psycopg2
import os
from dotenv import load_dotenv


# ------------------------------------
# Create DB Connection
# ------------------------------------
def main():
    load_dotenv()
    db_url = os.getenv("DB_URL")

    if not db_url:
        raise Exception("DB_URL not found in environment variables")

    conn = psycopg2.connect(db_url)
    query_sql = 'SELECT VERSION()'
    cur = conn.cursor()
    cur.execute(query_sql)
    version = cur.fetchone()
    print(f"Connected to PostgreSQL: {version[0]}") 
    return conn


# ------------------------------------
# Execute DDL
# ------------------------------------
def execute_ddl(conn, table_name, columns):
    #create a table with the given name and columns
    #columns: list of tuples (column_name, data_type)
    cols = ", ".join([f"{col_name} {data_type}" for col_name, data_type in columns])
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});"

    with conn.cursor() as cur:
        cur.execute(sql)
        conn.commit()
 
def create_table_gaurav(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gaurav_emp (
                id SERIAL PRIMARY KEY,
                course_name VARCHAR(50) UNIQUE,
                trainer VARCHAR(100),
                price INTEGER,
                duration INTEGER
            );
        """)
        conn.commit()                   
                       
# ------------------------------------
# Execute DQL (SELECT)
# ------------------------------------
def execute_dql(conn, query, params=None):
    #EXECUTE a query and return all results
    with conn.cursor() as cur:
        cur.execute(query, params or ())
        result = cur.fetchall()
    return result


# ------------------------------------
# Execute DML (INSERT)
# ------------------------------------
def execute_dml(conn, data):
    #INSERT data into gaurav_emp table
    with conn.cursor() as cur:
        for course_name, details in data.items():
            cur.execute("""
                INSERT INTO gaurav_emp (course_name, trainer, hours, price)
                VALUES (%s, %s, %s, %s )
                ON CONFLICT (course_name) DO NOTHING;
            """, (course_name, details['trainer'],details['hours'], details['price']))
        conn.commit()
if __name__ == "__main__":
    main()
