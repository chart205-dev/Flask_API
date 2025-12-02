from flask import Flask, jsonify, request
from logic import (
    fetch_all_users,
    fetch_user_by_id,
    insert_user,
    update_user,
    delete_user_by_id
)

app = Flask(__name__)


# ---------------------------
# GET（全ユーザー）
# ---------------------------
@app.route("/users", methods=["GET"])
def get_users():
    users = fetch_all_users()
    return jsonify(users), 200


# ---------------------------
# GET（1ユーザー）
# ---------------------------
@app.route("/users/<int:userid>", methods=["GET"])
def get_user(userid):
    user = fetch_user_by_id(userid)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# ---------------------------
# POST（ユーザー作成）
# ---------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    name = data.get("name")
    age = data.get("age")

    new_user = insert_user(name, age)
    return jsonify(new_user), 201


# ---------------------------
# PUT（ユーザー更新）
# ---------------------------
@app.route("/users/<int:userid>", methods=["PUT"])
def update_user_api(userid):
    data = request.json
    name = data.get("name")
    age = data.get("age")

    updated = update_user(userid, name, age)
    if updated:
        return jsonify(updated), 200

    return jsonify({"error": "User not found"}), 404


# ---------------------------
# DELETE（ユーザー削除）
# ---------------------------
@app.route("/users/<int:userid>", methods=["DELETE"])
def delete_user_api(userid):
    delete_user_by_id(userid)
    return jsonify({"message": f"User {userid} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
