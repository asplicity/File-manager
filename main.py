import os
from termcolor import cprint
import keyboard
import platform
import shutil

MAX_FILENAME_LENGTH = 8
os.chdir("C:\\Users")
selected_file_index = 0

while True:
    width, height = shutil.get_terminal_size()
    print(f"Current Directory:{os.getcwd():>50}")
    FilesAndDirectories = os.listdir()


    for i, File in enumerate(FilesAndDirectories):
        string = f"{File[:MAX_FILENAME_LENGTH] + '..' if len(File) > MAX_FILENAME_LENGTH else File:<10} {'dir' if os.path.isdir(File) else 'file':>50}"
        if i < selected_file_index + (height - 2) // 2 and i > selected_file_index - (height - 2) // 2:
            if i == selected_file_index:
                cprint(string, "white", "on_red")
            else:
                print(string)

    Event = keyboard.read_event(suppress=True)
    print(Event)

    if Event.event_type == keyboard.KEY_DOWN:
        if Event.name == "k" and selected_file_index > 0:
            selected_file_index -= 1
        elif Event.name == "j" and selected_file_index < len(FilesAndDirectories):
            selected_file_index += 1
        elif Event.name == "backspace":
            os.chdir(os.path.dirname(os.getcwd()))
            selected_file_index = 0
        elif Event.name == "enter" and os.path.isdir(FilesAndDirectories[selected_file_index]):
            os.chdir(FilesAndDirectories[selected_file_index])
            selected_file_index = 0
        elif Event.name == "enter" and os.path.isfile(FilesAndDirectories[selected_file_index]):
            os.startfile(FilesAndDirectories[selected_file_index])
            break #because it supress keystrokes even when in other windows
        elif Event.name == "q":
            break
    
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")