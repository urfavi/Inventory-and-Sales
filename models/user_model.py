import psycopg2
from psycopg2 import sql

def get_db_connection():
    conn = psycopg2.connect(
        dbname="inventory_sales_system",
        user="postgres",
        password="Agjc101404!",
        host="localhost"
    )
    return conn

def get_user_by_username(username):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT user_acc_id, user_acc_password_hash, user_acc_role, security_question, security_answer 
            FROM user_account 
            WHERE user_acc_username = %s
        """)
        cursor.execute(query, (username,))
        
        user = cursor.fetchone()
        
        print(f"\n[DATABASE DEBUG] Retrieved user {username}: {user}")
        
        cursor.close()
        conn.close()
        return user
    except Exception as e:
        print(f"[DATABASE ERROR] in get_user_by_username: {e}")
        return None

def update_user_password(username, hashed_str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE user_account 
            SET user_acc_password_hash = %s 
            WHERE user_acc_username = %s
            """, (hashed_str, username))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Update error: {e}")
        return False