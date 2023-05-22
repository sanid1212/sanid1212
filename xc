@echo off
set "source_folder=C:\path\to\source\folder"
set "destination_folder=C:\path\to\destination\folder"

echo Copying files...

for /r "%source_folder%" %%F in (*.cs *.csproj) do (
    set "file=%%~nxF"
    setlocal enabledelayedexpansion
    if "!file:~0,2!" == "~$" (
        endlocal
    ) else (
        echo %%F
        copy "%%F" "%destination_folder%"
        endlocal
    )
)

echo All files copied successfully.
