import json
from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji
import sys
import datetime
import os 

# redundant imports that might be used later if a system for saving to user defined file paths is added
# import tkinter as tk
# from tkinter import filedialog

WIDTH = 1777
HEIGHT_INIT = 231
HEIGHT_MODIF = 80

COLOUR = (54, 57, 63, 255)
PROFILE_WIDTH = 120

# Function to generate discord messages
def generate_discord_message(user, messages, time):
    # dynamically resizes the image as more messages are added
    HEIGHTS = [HEIGHT_INIT + i * HEIGHT_MODIF for i in range(len(messages))]
    
    # create image object and draw object
    img = Image.new('RGB', (WIDTH, HEIGHTS[len(messages) - 1]), color=COLOUR)
    draw = ImageDraw.Draw(img)

    # use the profile pic dictionary to find the correct pfp
    
    with open('profile_img/profpic_dict.json') as file:
    # with open('profpic_dict.json') as file:
        profpic_dict = json.loads(file.read())

    # add profile picture
    add_profpic(profpic_dict[user], img)

    # draw username on image
    add_username_time(user, draw, time)

    # draw message onto image
    add_message(messages, img)

    # save the image
    save_message(img,user,'test')

# Function to add a profile pic to the template
def add_profpic(file, background):

    profpic = Image.open(file)
    # set profile pic dimensions 
    profpic.thumbnail([sys.maxsize, PROFILE_WIDTH])

    # create a mask so that the profile pic displays as a circle
    mask = Image.new("L", profpic.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0,0),(PROFILE_WIDTH, PROFILE_WIDTH)], fill = 255)

    # paste the profile pic onto the background
    PROFPIC_POS = (36,45)
    background.paste(profpic, PROFPIC_POS, mask)

# function to add username and time to template
def add_username_time(name, background, message_time):

    # set values for username
    NAME_POS = (190,53)
    NAME_FONT_COLOUR = (255, 255, 255)
    NAME_FONT_SIZE = 50
    name_font = ImageFont.truetype('fonts/whitneymedium.otf', NAME_FONT_SIZE)

    # draw the user name on given these parameters
    background.text(NAME_POS, name, font=name_font, fill=NAME_FONT_COLOUR)

    # set values for time
    TIME_FONT_COLOUR = (180, 180, 180)
    TIME_FONT_SIZE = 30
    TIME_POS_Y = 67 # coordinates cannot be defined here as x changes with name length
    TIME_SPACING = 25
    time_font = ImageFont.truetype('fonts/whitneymedium.otf', TIME_FONT_SIZE)

    # find x coordinate for time text by using the name pos x and then adding the name
    #  length to it and then adding a small space in between the name and time
    time_pos = (NAME_POS[0] + name_font.getlength(name) + TIME_SPACING, TIME_POS_Y)

    # used current time to display on the message
    # changed that so that the messages have times that are offset from each other to make it more realistic
    # formatting time into HH:MM AM/PM
    time = message_time.strftime('%I:%M %p')
    time_text = f'Today at {time}'

    # draw the time given these parameters
    background.text(time_pos, time_text, font=time_font, fill=TIME_FONT_COLOUR)

# Function that adds message text to the image
def add_message(messages, background):

    # stage values to instantiate the text
    MESSAGE_X = 190
    MESSAGE_Y_INIT = 130
    MESSAGE_Y_MODIF = 80

    # message pos is dynamically changed to account for multiple messages being sent by one person
    MESSAGE_POS = [(MESSAGE_X, MESSAGE_Y_INIT + i * MESSAGE_Y_MODIF) for i in range(len(messages))]
    MESSAGE_FONT_COLOUR = (220, 220, 220)
    MESSAGE_FONT_SIZE = 50
    message_font = ImageFont.truetype('fonts/whitneybook.otf', MESSAGE_FONT_SIZE)

    # loop through the messages list and then add each message with a modest vertical offset
    for i in range(len(messages)):
        with Pilmoji(background) as pilmoji:
            pilmoji.text(MESSAGE_POS[i], messages[i], font=message_font, fill=MESSAGE_FONT_COLOUR)

# Function to save image to folder
def save_message(img, filename, folder):

    # create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # find number of files in folder to make ordering of images clearer
    num_files = len(os.listdir(folder))

    # save the image to a file
    img.save(os.path.join(folder, f'discord_message_{num_files}_{filename}.png'))

#Sample messages
# generate_discord_message('amogus', ['Hello World!'], datetime.datetime.now())
# generate_discord_message('discblue', ['This is a sample Discord message'], datetime.datetime.now())
# generate_discord_message('discred', ['Generated using PIL and Python', 'awagga', 'beep boop beep 🤓'], datetime.datetime.now())