import tkinter
from tkinter import *
from tkinter import filedialog
import customtkinter
from pytube import YouTube


def start_download():
    directory = filedialog.askdirectory(initialdir="C:/Downloads")
    yt_link = link.get()
    yt_object = YouTube(yt_link, on_progress_callback=on_progress)
    video = yt_object.streams.get_highest_resolution()
    title.configure(text=yt_object.title, text_color="white")
    finish_label.configure(text="")
    video.download(output_path=directory)
    finish_label.configure(text="- Download complete -", text_color="green")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    percent = str(int(percentage_of_completion))
    progress_percentage.configure(text=percent + "%")
    progress_percentage.update()

    # Update progressbar
    progress_bar.set(float(percentage_of_completion) / 100)


# Appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App frame
app = customtkinter.CTk()
app.geometry("480x300")
app.title("Youtube downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert YouTube-link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Download button
download = customtkinter.CTkButton(
    app, text="Select directory and download", command=start_download
)
download.pack(padx=10, pady=10)

# Progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=350)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Progress
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

# Run app
app.mainloop()
