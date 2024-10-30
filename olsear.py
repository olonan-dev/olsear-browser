
from msilib.schema import Icon
import sys
from turtle import clear
from typing import Self
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class MainWindow(QMainWindow):
      def __init__(self):
       super(MainWindow, self).__init__()
       self.browser = QWebEngineView()
       self.browser.setUrl(QUrl("https://olonan-dev.github.io/oslear-browser/"))
       self.setCentralWidget(self.browser)
       self.showMaximized()
       self.setWindowIcon(QIcon("oooo.png"))
       
       #navbar
       navbar = QToolBar()
       self.addToolBar(navbar)

       back_btn = QAction("back", self)
       back_btn.triggered.connect(self.browser.back)
       navbar.addAction(back_btn)

       forward_btn = QAction("forward", self)
       forward_btn.triggered.connect(self.browser.forward)
       navbar.addAction(forward_btn)

       reload_btn = QAction("reload", self)
       reload_btn.triggered.connect(self.browser.reload)
       navbar.addAction(reload_btn)

       home_btn = QAction("home", self)
       home_btn.triggered.connect(self.navigate_home)
       navbar.addAction(home_btn)

       self.url_bar = QLineEdit()
       self.url_bar.returnPressed.connect(self.navigate_to_url)
       navbar.addWidget(self.url_bar)

       self.browser.urlChanged.connect(self.update_url)



      def navigate_home(self):
          self.browser.setUrl(QUrl("https://olonan-dev.github.io/oslear-browser/"))

      def navigate_to_url(self):
          url = self.url_bar.text()
          self.browser.setUrl(QUrl(url))

      def update_url(self, q):
          self.url_bar.setText(q.toString())
    

 


app = QApplication(sys.argv)
QApplication.setApplicationName("Olsear")
window = MainWindow()
app.exec_()  