import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Every UI has a MainWindows that contains everything. 
class HelloWorld(QMainWindow):

  # We setup the window's title, size, and show it.
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.resize(1920, 1080)
    self.show()

# This is the "tamplate" to start the UI, just copy it.
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = HelloWorld()
  sys.exit(app.exec_())