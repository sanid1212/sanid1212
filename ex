@echo off
setlocal enabledelayedexpansion

set "root_directory=C:\your\root\directory"
set "keywords=password= pass=your_keyword1=your_keyword2="

for /r "%root_directory%" %%G in (*.cs *.csproj) do (
    set "file_path=%%~G"
    for %%K in (%keywords%) do (
        findstr /i /c:"%%K" "!file_path!" >nul 2>&1
        if !errorlevel! equ 0 (
            echo Keyword: %%K
            echo File: !file_path!
            echo.
        )
    )
)

pause