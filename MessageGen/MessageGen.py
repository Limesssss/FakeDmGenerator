import datetime
import tkinter as tk
from tkinter import filedialog
import DiscordMessage

def file_open():
    # create a tkinter instance
    root = tk.Tk()
    # hide the main tkinter dialogue
    root.withdraw()
    # set the file explorer to be on top
    root.attributes('-topmost', True)
    # set filepath to be the path of the file that is selected
    filepath = filedialog.askopenfilename()

    # get all the lines in the text file the encoding is set to utf-8 in order to handle emojis
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.read().splitlines()


    messages = []
    message_time = datetime.datetime.now()
    pause = 0
    # as the script follows a strict format that format can be utilised to split the script up
    for line in lines:
        # to catch if the line does not have a character that can be accessed with line[0]
        if line == "":
            continue
        # based on the text file format this is the flag used to see if a time is input
        if line[0] == 'T':
            pause = line.split(":")[1].strip()
        # based on the text file format this is the flag used to see if a user is input
        if line[0] == 'U':
            messages = []
            user = line.split(":")[1].strip()
        # based on the text file format this is the flag used to see if a message is input
        if line[0] == "M":         
            messages.append(line.split(":")[1].strip())
            # assumes that messages are always after users and then passes in the user and message list to the image maker
            DiscordMessage.generate_discord_message(user, messages, message_time)    
        else:
            continue
        message_time += datetime.timedelta(0,int(pause))

file_open()