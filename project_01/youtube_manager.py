# Here we Create an project like To do List type.
import json
    

def load_data():
    try:
        with open('Youtube_vedios.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_help(videos):
    with open('Youtube_vedios.txt', 'w') as file:
        json.dump(videos, file )

def list_all_videos(videos):
    print('\n')
    print('*' * 20)
    print('\n')
    print("List of all YouTube Vedios:")
    for index , video in enumerate(videos , start= 1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print('\n')
    print('*' * 20)

def add_vedio(videos):
    name = input("Enter Vedio name: ")
    time = input("Enter vedio time: ")
    videos.append({'name': name, 'time': time})
    print("Video added successfully.")
    save_data_help(videos)

def update_vedio(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new Vedio name: ")
        time = input("Enter new vedio time: ")
        videos[index - 1] = {'name': name, 'time': time} # Here we use index - 1 because list start with 0 and we want to update the correct index and our list index started from 1.
        print("Video updated successfully.")
    else:
        print("Invalid index.")
    save_data_help(videos)
def delete_vedio(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1] 
        print("Video deleted successfully.")
    else:
        print("Invalid index.")
    save_data_help(videos)

def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager! Choice your option:")
        print("1. List all YouTube Vedios.")
        print("2. Add YouTube Vedios.")
        print("3. Update a YouTube Vedios details.")
        print("4. Delete a YouTube Vedios.")
        print("5. Exit the App.")

        # Here use type actually what's he want to get 
        choice = input("Enter your choice: ")

        # print(videos)

        # When we have multiple option and want do select after verify the condition use "match" but we also use "If" statement way 
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_vedio(videos)
            case '3':
                update_vedio(videos)
            case '4':
                delete_vedio(videos)
            case '5':
                break
            # If any user enter other value from choice value then it cover in this line. Its like default value.
            case __: 
                print("Invalid Choice")
if __name__ == "__main__":
    main()