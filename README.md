# Vagrant File support

## Required install

### choco
For Windows.
For install python.
```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco upgrade chocolatey
```

### python
```
choco install python --version 3.6.5 -y
```

#### python packages
- For GUI

```
pip install --upgrade pip
pip install pyqt5
pip install pyqt5-tools
```
