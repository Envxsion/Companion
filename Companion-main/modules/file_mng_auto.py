import os 
import sys
import time
import shutil
import logging
from os import *
from curses import wrapper
from os.path import splitext, exists
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

dir_path = 'C:/Users/cyn0v/Downloads' #path to sort
dir_audio_path = 'C:/Users/cyn0v/Downloads/Audio' #audio
dir_video_path = 'C:/Users/cyn0v/Downloads/Video' #video
dir_image_path = 'C:/Users/cyn0v/Downloads/Images' #images
dir_document_path = 'C:/Users/cyn0v/Downloads/Documents' #pdf/word/ppts
dir_compressed_path = 'C:/Users/cyn0v/Downloads/Compressed' #zip files

def file_rename(path):
    filename, extension = splitext(path)
    counter = 1
    while exists(path):
        path = f"{filename} ({counter}){extension}"
        counter += 1

    return path

def move(dest, entry, file_name): #destination to move file, the file, name of file to check if it exists
    file_detected = os.path.exists(dest + "/" + file_name)
    if file_detected:
        rename = file_rename(file_name)
        os.rename(entry, rename)
    try: 
        shutil.move(entry, dest)
    except AttributeError:
        pass
    

def move_criteria(LoggingEventHandler): 
    with os.scandir(dir_path) as entries:
        for entry in entries:
            file_name = entry.name
            dest = ''
            if file_name.endswith('.wav') or file_name.endswith('.mp3'): 
                dest = dir_audio_path
                move(dest, entry, file_name)
            elif file_name.endswith('.mp4') or file_name.endswith('.mov'): 
                dest = dir_video_path
                move(dest, entry, file_name)
            elif file_name.endswith('.jpeg') or file_name.endswith('.png'):
                dest = dir_image_path
                move(dest, entry, file_name)
            elif file_name.endswith('.docx') or file_name.endswith('.pptx') or file_name.endswith('.pdf') or file_name.endswith('".xlsx"') or file_name.endswith('".txt"'):
                dest = dir_document_path
                move(dest, entry, file_name)
            elif file_name.endswith('.zip') or file_name.endswith('.rar'):
                dest = dir_compressed_path
                move(dest, entry, file_name)

def auto_file_main(stdscr):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = dir_path
    event_handler = move_criteria(LoggingEventHandler)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
