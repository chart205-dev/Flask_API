import json
import psycopg2

# 設定ファイルを読み込む
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# PostgreSQLに接続
def get_connection():
	connection = psycopg2.connect(
		host=config["host"],
		dbname=config["dbname"],
		user=config["user"],
		password=config["password"]
	)
	return connection

if __name__ == "__main__":
	print("✅ PostgreSQL に正常に接続できました！")