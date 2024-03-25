import tkinter as tki
from pytube import YouTube

def download_video():
    pass


def on_progress(stream, chunk, bytes_remaining):
    pass

# Base UI
app = tki.Tk()
app.title("Video & Audio Downloader")

link_var = tki.StringVar()
link_entry = tki.Entry(textvariable=link_var)
link_entry.pack()