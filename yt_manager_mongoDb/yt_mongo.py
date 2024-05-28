from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("")
print(client)
db = client["ytmongo"]

video_collections = db["videos"]

print(video_collections)

def list_videos():
    for video in video_collections.find():
        print(f"Id: {video['_id']}, name:{video['name']} , duration: {video['time']}")

def add_video():
    name = input("Enter your video name: ")
    time = input("Enter your video time: ")
    video_collections.insert_one({"name": name , "time": time})
def update_video():
    video_id = input("Enter your video id to update: ")
    name = input("Enter your video name: ")
    time = input("Enter your video time: ")
    video_collections.update_one({'_id':ObjectId(video_id)},{"$set":{"name":name , "time":time} })

def delete_video():
    video_id = input("Enter your video id to delete: ")
    video_collections.delete_one({"_id":ObjectId(video_id)})
def main():
    while True:
        print("\n Youtube Mangaer")
        print("1. List a All videos")
        print("2. Add a youtube video")
        print("3. delete a youtube video")
        print("4. upadte a youtube video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                add_video()
            case "3":
                delete_video()
            case "4":
                update_video()
            case "5":
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()