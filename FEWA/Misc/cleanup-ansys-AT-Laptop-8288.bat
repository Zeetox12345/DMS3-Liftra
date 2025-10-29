@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 27976)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 35804)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 25832)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 8288)

del /F cleanup-ansys-AT-Laptop-8288.bat
