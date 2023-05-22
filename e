@echo off
setlocal enabledelayedexpansion

set "root_directory=C:\your\root\directory"
set "keywords=password= pass=your_keyword1=your_keyword2="

for /r "%root_directory%" %%G in (*.cs *.csproj) do (
    for %%K in (%keywords%) do (
        findstr /i /m "%%K" "%%G" >nul 2>&1
        if !errorlevel! equ 0 (
            echo %%G
            exit /b
        )
    )
)

pause
