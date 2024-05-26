import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dum(videos,file)
def list_videos(videos):
    pass

def add_video(videos):
    pass

def delete_video(videos):
    pass

def update_video(videos):
    pass
def main():
    videos = load_data()
    while True:
        print("\n Youtube Mangaer")
        print("1. List a favourite video")
        print("2. Add a youtube video")
        print("3. delete a youtube video")
        print("4. upadte a youtube video")
        print("5. Exit")

        choices = input("choose a list of Commands")

        match choices:
            case "1":
                list_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                delete_video(videos)
            case "4":
                update_video(videos)
            case "5":
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()