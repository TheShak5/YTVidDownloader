# Import statements
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
download_path = '/Users/patel/Downloads'

print("Title: ", yt.title) # title of the YouTube Video

print("View: ", yt.views) # number of views the video has

yd = yt.streams.get_highest_resolution() # getting highest resolution of the given video

# ADD FOLDER HERE
yd.download(download_path) # downloading the video to the given download path