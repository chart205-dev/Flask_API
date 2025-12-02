from flask import Flask, request
import json
import psycopg2

#
app = Flask(__name__)

# 設定ファイルを読み込む
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# PostgreSQLに接続
connection = psycopg2.connect(
    host=config["host"],
    dbname=config["dbname"],
    user=config["user"],
    password=config["password"]
)

print("✅ PostgreSQL に正常に接続できました！")

@app.route('/users', methods=["GET"])
def get_users():
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM users;")
		rows = cursor.fetchall()
		users = []
		for row in rows:
			users.append({"id":str(row[0]), "name": row[1]})
	return users

if __name__ == "__main__":
	app.run(debug=True)