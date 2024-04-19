import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.exceute("DELETE FROM videos WHERE id = ? ",(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Application with DB")
        print("1. Show list")
        print("2. Add video ")
        print("3. upodate video ")
        print("4. delete video ")
        print("5. exit video ")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video ID you want to update: ")
            name = input("Enter New video name")
            time = input("Enter New video time")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter video id you wan to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invaild Choice")            


if __name__ == "__main__":
    main()