import sqlite3

DB_NAME ="tasks.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    return conn


def create_table():
    conn=connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()


def add_task_db(title):
    conn=connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
    conn.commit()
    conn.close()

def list_tasks_db():
    conn=connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def get_task_by_id(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, completed FROM tasks WHERE id = ?",
        (task_id,)
    )
    task = cursor.fetchone()

    conn.close()
    return task

def complete_task_db(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()  

def delete_task_db(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()                  

