""" importing the QMessageBox class. This way each time we want to reference it we can use it directly."""
from PyQt5.QtWidgets import QMessageBox

"""Everytime we create a new popup window we need to create a new instance of QMessageBox.

msg = QMessageBox()
Then we can start changing some properties of the messagebox like the title and the text.

msg.setWindowTitle("Tutorial on PyQt5")
msg.setText("This is the main text!")
The method names are pretty intuitive so I'll pass on explaining them.

We will add some more to our messagebox later but for now lets test it out. To actually see the messagebox when we run the code we need to add one last line to the end of our method:

x = msg.exec_()  # this will show our messagebox"""


"""A nice feature that our message boxes have it the ability to add an icon!

msg.setIcon(QMessageBox.Critical)
List of Icons
- QMessageBox.Critical
- QMessageBox.Warning
- QMessageBox.Information
- QMessageBox.Question"""


"""List of Buttons
- QMessageBox.Ok
- QMessageBox.Open
- QMessageBox.Save
- QMessageBox.Cancel
- QMessageBox.Close
- QMessageBox.Yes
- QMessageBox.No
- QMessageBox.Abort
- QMessageBox.Retry
- QMessageBox.Ignore

We can add any combinations of these buttons to our message box by using the following:

msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ignore | QMessageBox.Cancel) # seperate buttons with "|"
We can also set the button that will be highlighted by default by using:

msg.setDefaultButton(QMessageBox.Ignore)  # setting default button to Cancel"""

"""To do this we need to create a new method/function that takes one argument. This argument will be the button widget that was clicked.

    def popup_clicked(self, i):
        print(i.text())  # will print out the text on the button clicked
No we can link our messagebox to trigger that method when any button is pressed.

msg.buttonClicked.connect(self.popup_clicked)
Now when we click a button on the messagebox it's text will be printed out to the console."""

"""Informative Text
This is the text that shows below the main text.

msg.setInformativeText("informative text, ya!")"""

# full_code
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    ...

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Question)
        # msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("informative text, ya!")

        msg.setDetailedText("details")

        msg.buttonClicked.connect(self.popup_button)

    def popup_button(self, i):
        print(i.text())

