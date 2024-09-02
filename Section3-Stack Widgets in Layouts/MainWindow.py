"""
This example shows how to stack labels and widgets
Run this file to see the window.
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWidgets import QLabel
from TextWidget import TextWidget
# Every UI has a MainWindows that contains everything. 
class MainWindow(QMainWindow):

  # We setup the window's title, size, and show it.
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.resize(1920, 1080)
    self.centralWidget = QWidget(self)
    self.mainLayout = QVBoxLayout(self)
    self.centralWidget.setLayout(self.mainLayout)

    self.textWidget1 = TextWidget()
    self.mainLayout.addWidget(self.textWidget1)
    self.textWidget2 = TextWidget()
    self.mainLayout.addWidget(self.textWidget2)
    
    # To display a widget, it must be set to the central widget.
    self.setCentralWidget(self.centralWidget)

    self.show()

# This is the tamplate to start the UI, just copy it.
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())