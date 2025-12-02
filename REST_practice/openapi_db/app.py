from flask import Flask, jsonify, request
from logic_crul import fetch_all_qa_history, fetch_qa_history_by_id, insert_qa, dict_data

app = Flask(__name__)



# ---------------------------
# GET（テーブル全部）
# ---------------------------
@app.route('/qa', methods=["GET"])
def get_table():
	return fetch_all_qa_history()

@app.route('/qa/<string:qa_id>', methods=["GET"])
def get_table_by_id(qa_id):
	qa = fetch_all_qa_history()
	if qa:
		return jsonify(dict_data(qa)), 200
	return jsonify({"error": "qa_id not found"}), 404

@app.route('/qa', methods=["POST"])
def post_qa():
	data = request.get_json()
	question_text = data.get("question_text")
	qa = insert_qa(question_text)
	if qa:
		return jsonify(dict_data(qa)), 200
	return jsonify({"error": "qa_id not found"}), 404


if __name__ == "__main__":
	app.run(debug=True)
