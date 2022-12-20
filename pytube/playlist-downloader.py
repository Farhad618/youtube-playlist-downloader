from pytube import Playlist

while True:	
	link = str(input("Enter the Playlist link: "))

	pl = Playlist(link)

	dirname=pl.title

	for x in pl.videos:
		print("Downloading: " + x.title)
		x.streams\
		.filter(progressive=True, file_extension='mp4')\
		.order_by('resolution').desc().first().download("./"+dirname)

	print("Downloading completed...")
