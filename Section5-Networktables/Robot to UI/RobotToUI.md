# Robot To UI
This section explains how to get a variable's value from networktables and
diaplay it on the UI.
## Robot Code
There is a provided robot code template in the folder NetworkTablesRobotCode.
Please run it in simulation. It will start a networktable server on localhost.
## Sample Code
### How to Run Sample Code
1. Run robot code in simulation.
2. Run MainWindow.py. You should see a increasing number in the window.
### DoubleDisplayLabel.py
This class is a customized QLable that displays a double variable retrieved from
the networktable server. More customized QLables can be found in the 
[DriverUI 2024](https://github.com/grt192/DriverUI2024/tree/main/Widgets/CustomWidgets/BaseWidgets)
repo.
### MainWindow.py
This class creates a main window that has the double display label on the window.
### NetworktableManager.py
This class is a helper class. It wraps pynetworktables and provides methods for
getting and sending values to the networktable server.
