@echo off
set "source_folder=C:\path\to\source\folder"
set "destination_folder=C:\path\to\destination\folder"

for /r "%source_folder%" %%F in (*.cs) do (
    xcopy "%%F" "%destination_folder%" /I /Y
)
