import sqlite3
con = sqlite3.connect("todo.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT ,
title TEXT NOT NULL,
done INTEGER DEFAULT 0,
creat_at DEFAULT CURRENT_TIMESTAMP
)
""")
con.commit()


def add_task():
    task = input("Enter  task : ")
    cur.execute("INSERT INTO tasks(title) VALUES(?)" , (task,))
    con.commit()
    print("Task added ")


def show_task():
   rows = cur.execute("SELECT id , title , done ,creat_at FROM tasks").fetchall()
   if not rows:
       print("\nNo tasks yet")
       return
   print("\n -----Your Tasks-----")
   for id , title , done ,creat_at in rows:
       mark = "[x]" if done else "[]"
       print(f"{id}. {mark} {title} {creat_at}")
   print("-------------------------")
   
    

def delete_task():
    show_task()
    task_id = input("Enter a number to delete : ")
    cur.execute("DELETE FROM tasks WHERE id = ?" , (task_id,))
    print("Task deleted")
    con.commit()

def mark_done(task_id):
    cur.execute("UPDATE tasks SET done =1 WHERE id = ?" , (task_id ,))
    con.commit()

def edit_task():
    show_task()
    change_num = input("Enter new Number : ")
    change_title = input("Enter new Title : ")
    cur.execute("UPDATE tasks SET title =?  WHERE id = ? ", (change_title , change_num ))
    print("Task edited")
    con.commit() 

def show_pending():
    rows = cur.execute("SELECT * FROM tasks WHERE done = 0")
    if not rows:
        print("\nNo tasks yet")
    print("\n -----Your Tasks-----")
    for id , title , done ,creat_at in rows:
        print(f"{id}  {title} {creat_at}")
       


while True:
    print("\n1. Add Task")
    print("2.Show Tasks")
    print("3.Delete Tasks")
    print("4.Mark Done")
    print("5.Edit Task")
    print("6.Pending Tasks")
    print("7.Exit")

    choice = input("Choose :")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        show_task()
        task_id = input("Enter a number to delete : ")
        mark_done(task_id)
    elif choice == "5":
        edit_task()
    elif choice == "6":
        show_pending()

    elif choice == "7":
        con.close()
        break

    else:
        print("Invalide choice ")

