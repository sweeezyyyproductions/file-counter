import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def rename_files():
    folder_path = folder_entry.get()
    if not os.path.isdir(folder_path):
        result_label.config(text="Invalid folder path")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time)
            new_filename = creation_date.strftime("%m%d%y") + "_" + filename
            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(file_path, new_file_path)

    result_label.config(text="Files renamed successfully!")

window = tk.Tk()
window.title("File Renamer-CreationDate")
window.geometry("400x150")

folder_label = tk.Label(window, text="Select Folder:")
folder_label.pack()

folder_entry = tk.Entry(window, width=40)
folder_entry.pack()

folder_button = tk.Button(window, text="Browse", command=lambda: folder_entry.insert(0, filedialog.askdirectory()))
folder_button.pack()

rename_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
