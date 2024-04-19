from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://videospy:videospy@cluster0.1nmhzym.mongodb.net/",tlsAllowInvalidCertificates=True)

db = client["vManager"]
video_collection = db["videos"]


def list_video():
    for video in video_collection.find():
        print(f"ID : {video['_id']}, Name : {video['name']} and Time : {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name":new_name,"time":new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Application with MongoDB")
        print("1. Show list")
        print("2. Add video ")
        print("3. upodate video ")
        print("4. delete video ")
        print("5. exit video ")
        choice = input("Enter your choice : ")
        
        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter name : ")
            time = input("Enter time :")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video id : ")
            name = input("Enter new name : ")
            time = input("Enter new time :")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter video id to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
            

if __name__ == "__main__":
    main()