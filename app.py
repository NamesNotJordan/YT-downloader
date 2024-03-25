import tkinter as tki
from pytube import YouTube

DEFAULT_DOWNLOAD = "home/jayden/downloads"
def download_video(destination = DEFAULT_DOWNLOAD):
    try:
        yt = YouTube(url=link_entry.get())
        yt_stream = yt.streams.get_highest_resolution()
        
        yt_stream.download(output_path=destination)
    except:
        print("Download did not work")
    print("download complete")




def testButton():
    print(link_entry.get())


# Base UI
app = tki.Tk()
app.title("Video & Audio Downloader")
app.minsize(width=500, height=300)


heading_label = tki.Label(text="Enter a youtube link")
heading_label.pack()

status_label = tki.Label(text="")
status_label.pack

download_button = tki.Button(text="Download", command=testButton)
download_button.pack()

link_var = tki.StringVar()
link_entry = tki.Entry(textvariable=link_var)
link_entry.pack()

app.mainloop()