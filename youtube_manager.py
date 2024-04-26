import sqlite3
con = sqlite3.connect('youtube.db')

cur = con.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_videos():
    name = input('Enter name: ')
    time = input('Enter time: ')



def update_videos():
    video_id = input('Enter video id: ')
    name = input('Enter name: ')
    time = input('Enter time: ')

def delete_videos():
    video_id = input('Enter video id: ')


def main():
    while True:
        print('\n Youtube manager app with SQLite3')
        print('1. List videos')
        print('2. Add videos')
        print('3. Update videos')
        print('4. Delete videos')
        print('5. Exit app')

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                add_videos()
            case '3':
                update_videos()
            case '4':
                delete_videos()
            case '5':
                break
            case _:
                break

if __name__ == "__main__":
    main()
