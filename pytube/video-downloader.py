from pytube import YouTube

while True:	
	link = str(input("Enter the Playlist link: "))

	yt = YouTube(link)

	print("Downloading: " + yt.title)

	yt.streams\
	.filter(progressive=True, file_extension='mp4')\
	.order_by('resolution').desc().first().download("./videos")

	print("Downloading completed...")
