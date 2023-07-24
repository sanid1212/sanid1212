@echo off
set "sigcheckPath=C:\Path\To\sigcheck64.exe"
set "rootFolder=C:\Path\To\Your\Folder"
set "outputFile=C:\Path\To\output.csv"

(for /r "%rootFolder%" %%F in (*.exe *.dll) do (
    "%sigcheckPath%" -nobanner -a -e -c "%%F"
)) > "%outputFile%"
