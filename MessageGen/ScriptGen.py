import sys
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from collections import Counter
import Helper

# create the main page1
app = QApplication([])
window = QMainWindow()
stackedWidget = QStackedWidget()
window.setCentralWidget(stackedWidget)

page1 = QWidget()
page1.setWindowTitle("Profile Pics")
# make the page1 always on top
page1.setWindowFlags(Qt.WindowStaysOnTopHint)
page1.resize(300,100)

# create a list to store the selected images and their names
images = []

# Function to save the images and their names to a JSON dictionary
def save_images_and_names():
    # clear the contents of the file
    with open("profile_img\profpic_dict.json", "w") as f:
        f.truncate(0)

    valid = True

    # create the JSON dictionary ensuring all names are unique and not null
    image_names = {}
    for image, name in images:
        key_counts = Counter(image_names)
        if name.text() != "" and key_counts[name.text()] == 0:
            image_names[name.text()] = image
        else:
            valid = False

    if valid == True:
        # write the dictionary to a file
        with open("profile_img\profpic_dict.json", "w") as f:
            # write the dictionary to the file in pretty-printed format
            json.dump(image_names, f, indent=4)
        # Helper.clear_widgets(page1)

    else:
        Helper.create_error_message("Users Need Unique Usernames")

# Function to handle the image selection and renaming
def select_and_rename_images():
    # open a file selection dialog and allow the user to select multiple images
    # also sets default file type to png/jpg
    selected_images, _ = QFileDialog.getOpenFileNames(page1, "Select Images", "", "Images (*.png *.jpg);;All files (*)")

    # iterate through the selected images and create a label and a text box for each image
    for image in selected_images:
        # create a label to display the image
        image_label = QLabel()
        # load and resize the image
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(120, 120, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)

        # create a text box to allow the user to enter a name for the image
        image_name = QLineEdit()
        image_name.setPlaceholderText("Enter Username")

        # add the image and its name to the list
        images.append((image, image_name))
        # add the label and text box to the layout
        layout.addWidget(image_label)
        layout.addWidget(image_name)

    # if at least two images have been selected, show the save button
    if len(images) >= 2:
        save_button.show()

page2 = QWidget()
layout2 = QGridLayout()
page2.setLayout(layout2)
button2 = QPushButton("Go to Page 1")
layout2.addWidget(button2, 0, 0)
stackedWidget.addWidget(page2)




# create a grid layout to hold the widgets
layout = QGridLayout()

# add the images and their corresponding text boxes in a grid
row = 1
col = 0

# iterate through the selected images and create a label and a text box for each image
for image, name in images:
    # create a label to display the image
    image_label = QLabel()
    # load and resize the image
    pixmap = QPixmap(image)
    pixmap = pixmap.scaled(120, 120, Qt.KeepAspectRatio)
    image_label.setPixmap(pixmap)

    # add the label and text box to the layout
    layout.addWidget(image_label, row, col)
    layout.addWidget(name, row, col + 1)

    # increment the row index
    row += 1
    
    # if the current row is the last row of the grid, reset the row index and increment the column index
    if row == layout.rowCount():
        row = 0
        col += 2


# create a button to trigger the image selection and renaming process
select_button = QPushButton("Select Images", page1)
select_button.clicked.connect(select_and_rename_images)

# create a button to trigger the saving of the images and their names to a JSON dictionary
save_button = QPushButton("Save Profiles and Continue", page1)
save_button.clicked.connect(save_images_and_names)
save_button.clicked.connect(lambda: stackedWidget.setCurrentWidget(page2))
save_button.hide()  # Hide the button initially
# add the select button and save button to the grid layout
layout.addWidget(select_button, 0, 0)
layout.addWidget(save_button, 0, 1)

# set the layout for the main page1
page1.setLayout(layout)

# show the main page1
page1.show()

# run the main loop
sys.exit(app.exec_())