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
    cur.execute('SELECT * FROM videos')
    print('\n')
    print('_'*70)
    for row in cur.fetchall():
        print(row)
    print('_'*70)
    print('\n')

def add_videos():
    name = input('Enter name: ')
    time = input('Enter time: ')
    cur.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name,time))
    con.commit()
    print('\n \t Addition successful')



def update_videos():
    list_videos()
    video_id = input('Enter video id: ')
    name = input('Enter name: ')
    time = input('Enter time: ')
    cur.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, video_id))
    con.commit()
    print('\n \t Update successful')

def delete_videos():
    list_videos()
    video_id = input('Enter video id: ')
    cur.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    con.commit()
    print('\n \t Deletion successful')


def main():
    while True:
        print('\n Youtube manager app with SQLite3')
        print('1. List videos')
        print('2. Add videos')
        print('3. Update videos')
        print('4. Delete videos')
        print('5. Exit app')

        print('\n')

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
                pass
        
        input('Press enter to continue. ')

    con.close()

if __name__ == "__main__":
    main()

