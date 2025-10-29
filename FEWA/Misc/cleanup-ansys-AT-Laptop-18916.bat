@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 29560)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 27176)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 35448)
if /i "%LOCALHOST%"=="AT-Laptop" (taskkill /f /pid 18916)

del /F cleanup-ansys-AT-Laptop-18916.bat
