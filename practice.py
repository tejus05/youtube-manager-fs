import json

def list_all_videos(vidoes):
  for index, video in enumerate(vidoes, start=1):
    print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
  print("*"*50)

def add_video(videos):
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  videos.append({'name': name, 'time': time})
  save_data_helper(videos)

def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video to be updated: "))
  if 1 <= index <= len(videos):
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index-1] = {'name':name, 'time': time}
    save_data_helper(videos)
  else:
    print("Invalid index selected. ")

def delete_video(videos):
  index = int(input("Enter the video to be deleted: "))
  if 1 <= index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
    print("Invalid index selected. ")

def load_data():
    print("load data called")
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
  with open('youtube.txt','w') as file:
    json.dump(videos, file)

def main():

  videos = load_data()
  
  while True:
    print("Youtube Manager")
    print("1. List all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video detail")
    print("4.Delete a youtube video")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    match choice:
      case '1':
        list_all_videos(videos)
      case '2':
        add_video(videos)
      case '3':
        update_video(videos)
      case '4':
        delete_video(videos)
      case '5':
        break
      case _:
        print("Invalid Choice")

if __name__ == "__main__":
  main()