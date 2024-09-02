import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtWidgets import QLabel
from DoubleDisplayLabel import DoubleDisplayLabel
# Every UI has a MainWindows that contains everything. 
class MainWindow(QMainWindow):

  # We setup the window's title, size, and show it.
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.resize(1920, 1080)
    self.doubleDisplayLabel= DoubleDisplayLabel(
      "prarmeterName", "tableName", "entryName"
    )
    
    # To display a widget, it must be set to the central widget.
    self.setCentralWidget(self.doubleDisplayLabel)

    self.show()

# This is the "tamplate" to start the UI, just copy it.
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())