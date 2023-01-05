from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Some Error Occured")
    print("Download Successful!")

link = input("Enter URL Here::")
Download(link)