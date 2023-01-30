MessageGen is a tool that can be used to create screenshots of messages that make it look like a conversation has taken place.
For now it is simply being created following https://youtu.be/o4T7i_FIqy0 which creates this tool for discord messages.
Later on I want to add Messenger chats, Instagram dms, Text messages, Emails, Youtube comments and Reddit comments.

Files and uses
 - MessageGen\profile_img - contains the profile pictures that are being used in the codebase
 - MessageGen\profile_img\profpic_dict.json - dictionary of user names that links them to a profile pic (should be edited when new users and profile pics are to be used)
 - MessageGen\fonts - contains the fonts that are being used to replicate the style of the message to be sent
 - MessageGen\ProfileGen.py - used to allow users to add images and generate scripts in an easier format than making a txt file, also updates the profile pic json
 - MessageGen\MessageGen.py - used to read in a script file and then depending on the stlye that is to be used passes those values to that class
 - MessageGen\DiscordMessage.py - used to make a fake discord style message screenshot
 
Overall Use
 - Change script.txt or make a new .txt file that follows the same format
 - Add profile images to the folder profile_img and add username and the filepath for the image to profile_img\profpic_dict.json
 - Run MessageGen.py with python3 .\MessageGen.py
 - Select the script file when promted
 - See images in the new folder called test
 - Delete the test folder to run again without getting the images confused

Users can run ScriptGen.py instead of following step 2 of the Overall Use for a more guided experience

Currently Implementing
 - Creating a clean frontend so that users can simply follow a GUI that promts them through the steps defined in Overall Use as the use is fairly clunky right now.
 - Users can run ScriptGen.py instead of following step 2 of the Overall Use, however I want the whole thing to work more intuitively
