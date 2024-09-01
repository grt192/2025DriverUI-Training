import sys
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout 

class PushButtonWidget(QWidget):

  def __init__(self):
    super().__init__()

    self.layout = QVBoxLayout(self)
    # Defines a push button.
    self.pushButton = QPushButton("Click Me")
    # Links the click event to the onClick function.
    self.pushButton.clicked.connect(self.onClick)
    # Adds the button to the layout.
    self.layout.addWidget(self.pushButton)

  def onClick(self):
    print("Button Clicked")