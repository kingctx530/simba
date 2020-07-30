@echo off

%~dp0\7z.exe x -y %~dp0\gettext-tools-0.17.zip -oC:\gettext-tools-0.17
%~dp0\7z.exe x -y %~dp0\gettext-runtime-0.17-1.zip -oC:\gettext-tools-0.17
setx path "%PATH%;C:\gettext-tools-0.17\bin"

pause