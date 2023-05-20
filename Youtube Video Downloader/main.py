from pytube import YouTube

link = input("Please enter the video link:")
yt = YouTube(link)
yr = yt.streams.get_highest_resolution()

print("Your video is downloading please wait")
wait = 1
for i in range(3):
    print("{}/3".format(wait))
    wait += 1
yr.download()
print("Video downloaded successfully")