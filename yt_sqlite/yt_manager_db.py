import sqlite3

connection = sqlite3.connect("youtube_db")

cursor = connection.cursor()

cursor.execute(''' 
   CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY ,
               name TEXT NOT NULL,
               time TXET NOT NULL
   )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name , time ) VALUES  (? , ?)",(name,time))
    connection.commit()

def update_video(videoId, time ,name):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ? ", (name , time , videoId))
    connection.commit()

def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ? ", (videoId,))
    connection.commit()
def main():
    while True:

        print("\n Youtube manager")
        print("1. List a all video")
        print("2. Add a youtube video")
        print("3. delete a youtube video")
        print("4. upadte a youtube video")
        print("5. Exit App")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            add_video(name,time)

        elif choice == '3':
            videoId = input("Enter videoId to delete: ")
            delete_video(videoId)
        elif choice == '4':
            videoId = input("Enter video Id to update")
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            update_video(videoId,name,time)
        
        elif choice == '5':
            connection.close()
            break

        else:
            print("Invalid choice")


    



if __name__ == "__main__":
    main()