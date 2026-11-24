# Patched: SQL injection fixed using parameterised query
from flask import request
import sqlite3

@app.route('/users')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    return str(cursor.fetchall())
