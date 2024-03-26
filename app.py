import tkinter as tki
from pytube import YouTube

DEFAULT_DOWNLOAD = "home/jayden/downloads"


def download_video(destination = DEFAULT_DOWNLOAD):
    link = link_entry.get()
    audio_only = audio_only_state.get()
    try:
        yt = YouTube(url=link)
        if audio_only:
            yt_stream = yt.streams.get_audio_only()
        else:
            yt_stream = yt.streams.get_highest_resolution()
        yt_stream.download(output_path=destination)

    except Exception as e:
        status_label.config(text=f"Error {str(e)}")
    status_label.config(text="Download Complete")    


def testButton():
    print(link_entry.get())


# Base UI
app = tki.Tk()
app.title("Video & Audio Downloader")
app.minsize(width=500, height=300)


heading_label = tki.Label(text="Enter a youtube link")
heading_label.place(column=1,row=0)

status_label = tki.Label(text="")
status_label.place()


link_entry = tki.Entry()
link_entry.focus()
link_entry.place()

# TODO: add audio only selector
audio_only_state = tki.BooleanVar()
audio_only_check = tki.Checkbutton(text="Download audio only",variable= audio_only_state )

download_button = tki.Button(text="Download", command=testButton)
download_button.pack()


app.mainloop()