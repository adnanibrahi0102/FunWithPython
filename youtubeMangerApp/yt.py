import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos,file)
def list_videos(videos):
   print(videos)
   for index , video in enumerate(videos , start=1):
       print (f"{index}. {video['name']} ,Duration: {video['time']}")


def add_video(videos):
    name = input ("Enter video name: ")
    time = input ("Enter video time: ")
    videos.append({"name":name,"time":time})
    save_data(videos)

def delete_video(videos):
   list_videos(videos)
   index = int(input("Enter video index to delete: "))
   del videos[index-1]
   save_data(videos)


def update_video(videos):
    list_videos(videos)
    index = int(input("Enter video index to update: "))
    name = input ("Enter video name: ")
    time = input ("Enter video time: ")
    videos[index-1] ={"name":name, "time":time }
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