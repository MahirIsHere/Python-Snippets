"""After you create your UI save it and convert it to a python file using the following command:
"""
"""pyuic5 -x "filename".ui -o "filename".py
Next we will open our python file and add some methods to change the image source.
"""
"""To edit our image source we will use the following line.
self.photo.setPixmap(GtGUI.QPixmap("dog.jpg"))
# note: photo is the name of my label
# "dog.jpg" is a photo that is in the same directory as my python file
"""
"""We'll add some methods that we can call to change the image.

    def show_cat(self):
        self.photo.setPixmap(QtGUI.QPixmap("cat.jpg"))
    
    def show_dog(self):
        self.photo.setPixmap(QtGUI.Qpixmap("dog.jpg"))
And finally link our buttons to call them.

    def setupUI(self):
        ...
        self.dog.clicked.connect(self.show_dog) 
        self.cat.clicked.connect(self.show_cat)
"""
# Full Code
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("cat.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 510, 411, 41))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dog.clicked.connect(self.show_dog)
        self.cat.clicked.connect(self.show_cat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))

    def show_dog(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/dog.jpg"))

    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/cat.jpg"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
