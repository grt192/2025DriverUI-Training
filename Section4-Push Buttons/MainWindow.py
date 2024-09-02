"""
This example shows how to create a push button and connect it to a function.
Run this file to see the window.
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtWidgets import QLabel
from PushButtonWidget import PushButtonWidget
# Every UI has a MainWindows that contains everything. 
class MainWindow(QMainWindow):

  # We setup the window's title, size, and show it.
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.resize(1920, 1080)
    self.pushButtonWidget = PushButtonWidget()
    
    # To display a widget, it must be set to the central widget.
    self.setCentralWidget(self.pushButtonWidget)

    self.show()

# This is the "tamplate" to start the UI, just copy it.
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())