import sys
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from collections import Counter



#Helper function used to clear all widgets from window
def clear_widgets(window):
    for widget in window.findChildren(QWidget):
        widget.setParent(None)

# Helper function for front end error logging
def create_error_message(text):
    message_box = QMessageBox()
    message_box.setWindowTitle("Error")
    message_box.setWindowFlags(Qt.WindowStaysOnTopHint)
    message_box.setText(text)
    message_box.setIcon(QMessageBox.Critical)
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.exec_()