import sqlite3

con = sqlite3.connect("Youtube_vedio_details.db")

cur = con.cursor() # Create a cursor object to execute SQL commands means it allows us to interact with the database and execute SQL queries.

cur.execute(""" 
    CREATE TABLE IF NOT EXISTS Videos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
""")
def list_all_vedios():
    cur.execute("SELECT * FROM Videos") # It store \ Hold all the values in excute function.It return a tuple of all the rows in the Videos table.So, we need for loop to print all the rows one by one. 
    rows = cur.fetchall() # It fetches all the rows returned by the previous SQL query and stores them in the variable row. The result is a list of tuples, where each tuple represents a row from the Videos table.
    if rows: # It checks if there are any rows returned by the query. If there are rows, it proceeds to print their details; otherwise, it prints a message indicating that no videos were found in the database.
        print("*" * 10)
        for row in rows:
            print(f"id: {row[0]} | name: {row[1]} | time: {row[2]}") # It prints the details of each video in a formatted way. The row variable is a tuple, and we access its elements using indexing (row[0] for ID, row[1] for Name, and row[2] for Time).
    else:
        print("*" * 10)
        print("No videos found in the database.")

def add_vedios(name, time):
    cur.execute("INSERT INTO Videos(name, time) VALUES (?, ?)",(name, time)) # It inserts a new video into the Videos table. The SQL query uses placeholders (?) for the name and time values, which are provided as a tuple (name, time) in the second argument of the execute method. This helps prevent SQL injection attacks by ensuring that user input is properly escaped.
    con.commit() # It commits the changes to the database, making the new video entry permanent.

def update_vedios(name, time, Video_id):
    cur.execute("UPDATE Videos SET name = ?, time = ? WHERE id = ?", (name, time, Video_id))
    con.commit()
    print(f"Video with id {Video_id} has been updated successfully.")

def delete_vedios(Video_id):
    cur.execute("DELETE FROM Videos WHERE id = ?", (Video_id,))
    con.commit()
    print(f"Video with id {Video_id} has been deleted successfully.")

def main():
    while True:
        print("\n YouTube Manager With Database(sqlite3)! Choice your option:")
        print("1. List all YouTube Vedios.")
        print("2. Add YouTube Vedios.")
        print("3. Update a YouTube Vedios details.")
        print("4. Delete a YouTube Vedios.")
        print("5. Exit the App.")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_vedios()
        elif choice == "2":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            add_vedios(name, time)
        elif choice == "3":
            Video_id = input("Enter the id of the video to update: ")
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            update_vedios(name, time,Video_id)
        elif choice == "4":
            Video_id = input("Enter the id of the video to delete: ")
            delete_vedios(Video_id)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    con.close() # Close the database connection when the app is exited.
if __name__ == "__main__":
    main()