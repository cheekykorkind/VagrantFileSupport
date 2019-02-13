# Vagrant key support

## Required install

### choco
For Windows.
For install python and winscp.
```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco upgrade chocolatey
```

### python
```
choco install python --version 3.6.5 -y
```

#### python packages
- Send data from windows to linux.
- Execute linux command from windows.

```
pip install --upgrade pip
pip install pyqt5
pip install pyqt5-tools
```
