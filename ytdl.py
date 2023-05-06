import os
import pytube
import sys
import uuid

url = input("Please enter a YouTube video URL:\n>> ")

yt = pytube.YouTube(url)

print()
print("------- Video -------")
print("Channel:", yt.author)
print("Title:", yt.title)
print("Length (seconds):", yt.length)
print("Uploaded:", yt.publish_date)
print("---------------------")
print()

video = yt.streams.get_highest_resolution()
name = str(uuid.uuid4()) + ".mp4"

print("Downloading video...")

video.download("./", name)

print("\nDownloaded video!")
print("File Location:", os.getcwd() + "\\" + name)

print()
os.system("pause")
sys.exit()
