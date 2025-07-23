from db import get_connection

def add_task(description):
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        conn.commit()

def list_tasks():
    with get_connection() as conn:
        cursor = conn.execute("SELECT id, description, is_done FROM tasks")
        return cursor.fetchall()
    
def complete_task(task_id):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))
        conn.commit()