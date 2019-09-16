(echo cd %~dp0 && echo powershell -file .\src\setWallpaper.ps1) >> main.bat
SchTasks /Create /SC DAILY /TN "DailyWallpaper" /TR "%~dp0main.bat" /ST 09:00 /RL HIGHEST