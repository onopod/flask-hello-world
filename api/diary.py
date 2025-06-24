from flask import Blueprint, request, jsonify
import os
import pymysql
from pymysql.cursors import DictCursor


def get_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", ""),
        database=os.environ.get("DB_NAME", "test"),
        cursorclass=DictCursor,
        autocommit=True,
    )


diary_bp = Blueprint("diary", __name__)


@diary_bp.route("/diaries", methods=["GET"])
def get_diaries():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM Diary")
        diaries = cur.fetchall()
    conn.close()
    return jsonify(diaries)


@diary_bp.route("/diaries/<int:diary_id>", methods=["GET"])
def get_diary(diary_id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM Diary WHERE id = %s", (diary_id,))
        diary = cur.fetchone()
    conn.close()
    if diary:
        return jsonify(diary)
    return jsonify({"error": "Diary not found"}), 404


@diary_bp.route("/diaries", methods=["POST"])
def create_diary():
    data = request.get_json() or {}
    title = data.get("title")
    content = data.get("content")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO Diary (title, content) VALUES (%s, %s)",
            (title, content),
        )
        diary_id = cur.lastrowid
    conn.close()
    return jsonify({"id": diary_id, "title": title, "content": content}), 201


@diary_bp.route("/diaries/<int:diary_id>", methods=["PUT"])
def update_diary(diary_id):
    data = request.get_json() or {}
    title = data.get("title")
    content = data.get("content")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE Diary SET title=%s, content=%s WHERE id=%s",
            (title, content, diary_id),
        )
        updated = cur.rowcount
    conn.close()
    if updated:
        return jsonify({"id": diary_id, "title": title, "content": content})
    return jsonify({"error": "Diary not found"}), 404


@diary_bp.route("/diaries/<int:diary_id>", methods=["DELETE"])
def delete_diary(diary_id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM Diary WHERE id=%s", (diary_id,))
        deleted = cur.rowcount
    conn.close()
    if deleted:
        return jsonify({"result": "success"})
    return jsonify({"error": "Diary not found"}), 404
