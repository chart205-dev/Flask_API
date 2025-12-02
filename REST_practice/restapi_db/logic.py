from db import get_connection

def run_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params)

        # SELECT の場合だけ cursor.description が存在する
        if cursor.description is not None:
            rows = cursor.fetchall()
        else:
            rows = None

        conn.commit()
        return rows

    finally:
        cursor.close()
        conn.close()


# ---------------------------
# CRUD 関数
# ---------------------------

def fetch_all_users():
    query = "SELECT id, name, age FROM users ORDER BY id"
    return run_query(query)


def fetch_user_by_id(userid):
    query = "SELECT id, name, age FROM users WHERE id = %s"
    rows = run_query(query, (userid,))
    return rows[0] if rows else None


def insert_user(name, age):
    query = """
        INSERT INTO users (name, age)
        VALUES (%s, %s)
        RETURNING id, name, age;
    """
    rows = run_query(query, (name, age))
    return rows[0] if rows else None


def update_user(userid, name, age):
    query = """
        UPDATE users SET name = %s, age = %s
        WHERE id = %s
        RETURNING id, name, age;
    """
    rows = run_query(query, (name, age, userid))
    return rows[0] if rows else None


def delete_user_by_id(userid):
    query = "DELETE FROM users WHERE id = %s"
    run_query(query, (userid,))
    return True
