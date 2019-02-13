@ECHO off
SET sharedFolder=C:\Users\IEUser\Desktop\work
SET MainFileName=Main

REM Use --onefile option after convert ui to py. 
pyuic5 "View/Ui_MainWindow.ui" -o "View/Ui_MainWindow.py"

REM Use -windowed for noconsole
pyinstaller --windowed --onefile --distpath "./Product" %MainFileName%.py

REM VagrantSupport
move %sharedFolder%\src\Product\%MainFileName%.exe %sharedFolder%\src\Product\VagrantSupport.exe

REM clean up
rmdir /s /q %sharedFolder%\src\__pycache__
rmdir /s /q %sharedFolder%\src\build
del /q %sharedFolder%\src\%MainFileName%.spec

pause