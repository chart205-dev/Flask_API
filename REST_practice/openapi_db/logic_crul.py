import json
from db import get_connection
from logic_openai import answer_by_chatgpt

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

def dict_data(data):
    dict_data = {
		"id": data[0]
		# "question_text": data[1]
		# "answer_text": data[2],
		# "created_at": data[3]
	}
    return dict_data

# ---------------------------
# CRUD 関数
# ---------------------------
def fetch_all_qa_history():
    query = "SELECT * FROM qa_history ORDER BY id"
    table = run_query(query)
    return table

def fetch_qa_history_by_id(qa_id):
    query = "SELECT * FROM qa_history WhERE id = %s"
    table = run_query(query, (qa_id,))
    return table[0] if table else None

def insert_qa(question_text):
    query = """
        INSERT INTO qa_history (question_text, answer_text)
        VALUES (%s, %s)
        RETURNING id, question_text, answer_text;
	"""
    answer_text = answer_by_chatgpt(question_text)
    table = run_query(query, (question_text, answer_text))
    return table[0] if table else None

if __name__ == "__main__":
     print("エラーなし")