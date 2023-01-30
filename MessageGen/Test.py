from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QVBoxLayout, QWidget

# Create the main window and stacked widget
app = QApplication([])
window = QMainWindow()
stackedWidget = QStackedWidget()
window.setCentralWidget(stackedWidget)

# Create the first page
page1 = QWidget()
layout1 = QVBoxLayout()
page1.setLayout(layout1)
button1 = QPushButton("Go to Page 2")
layout1.addWidget(button1)
stackedWidget.addWidget(page1)

# Create the second page
page2 = QWidget()
layout2 = QVBoxLayout()
page2.setLayout(layout2)
button2 = QPushButton("Go to Page 1")
layout2.addWidget(button2)
stackedWidget.addWidget(page2)

# Connect the buttons to the stacked widget
button1.clicked.connect(lambda: stackedWidget.setCurrentWidget(page2))
button2.clicked.connect(lambda: stackedWidget.setCurrentWidget(page1))

window.show()
app.exec_()