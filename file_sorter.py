import os
import mimetypes
import shutil

# FILL IN BELOW
# source folder e.g. Windows: "C:\\Users\\UserName\\Downloads"

source_folder = ""
dest_folder_audio = ""
dest_folder_video = ""
dest_folder_image = ""
dest_folder_other = ""

# move files to folder by type

def moveHandler(path, mime_type):
    if mime_type.startswith('image'):
        shutil.move(path, dest_folder_image)
    elif mime_type.startswith('audio'):
        shutil.move(path, dest_folder_audio)
    elif mime_type.startswith('video'):
        shutil.move(path, dest_folder_video)
    else:
        shutil.move(path, dest_folder_other)


# scan all file in source folder

with os.scandir(source_folder) as files:
    for file in files:
        mime_type, _ = mimetypes.guess_type(file.name)
        path = source_folder + "/" + file.name
        moveHandler(path, mime_type) 