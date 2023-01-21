from pytube import YouTube
def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
dlink = input("url")
download(dlink) 
print("Download is completed successfully")
