import sys
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

class TextWidget(QWidget):

  def __init__(self):
    super().__init__()
    # Qlabel is the basic component, it can be customized for different
    # purposes.
    self.textLabel = QLabel("Hello World", self)