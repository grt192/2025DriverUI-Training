import sys
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

class TextWidget(QWidget):

  def __init__(self):
    super().__init__()

    # QVBoxLayout stacks widgets vertically.
    # Try changing it to QHBoxLayout to see the difference.
    self.layout = QVBoxLayout(self)

    # Qlabel is the basic component, it can be customized for different
    # purposes.
    self.textLabel1 = QLabel("Hello World1", self)
    self.layout.addWidget(self.textLabel1) #Add this label to layout

    self.textLabel2 = QLabel("Hello World2", self)
    self.layout.addWidget(self.textLabel2) 

    self.textLabel3 = QLabel("Hello World3", self)
    self.layout.addWidget(self.textLabel3)