"""Snippet/Framework whatever you would call it but this is not the correct oop implementation it's precedure"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) #(x,y,width,height) 
    win.setWindowTitle("My first window!") 
    
    label = QLabel(win)
    label.setText("my first label") #header
    label.move(50, 50)  #(x,y) inside win

    win.show()
    sys.exit(app.exec_())

main()  # make sure to call the function