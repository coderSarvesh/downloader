import tkinter as tk
from pytube import YouTube
import re 

root=tk.Tk()
root.geometry("300x200")

def download():
    print(dlink.get())
    youtubeObject = YouTube(dlink.get())
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        # print("Download Successfull")
        vidsuccess_label = tk.Label(root, text = 'Video Download Complete').grid(row=5)
    except Exception as e: print(e)

def downloadAudio():
    print(dlink.get())
    ytObj = YouTube(dlink.get())
    ytObj = ytObj.streams.filter(only_audio=True).first()
    try:
        ytObj.download()
        success_label = tk.Label(root, text = 'Audio Download Complete').grid(row=4)
    except Exception as e: print(e)

name_label = tk.Label(root, text = 'Enter URL')
dlink = tk.Entry(root, width=40)
video_btn=tk.Button(root,text = 'Download Video', command = download,pady=10,padx=10)
audio_btn=tk.Button(root,text = 'Download Audio', command = downloadAudio,pady=10,padx=10)

name_label.grid(row=0,column=0)
dlink.grid(row=0,column=1)
video_btn.grid(row=1,column=0,columnspan=2,rowspan=1,ipadx=10,ipady=10)
audio_btn.grid(row=2,column=0,columnspan=2,rowspan=2,ipadx=10,ipady=10)
root.resizable(width=False, height=False)
root.mainloop()

