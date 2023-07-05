@echo off
setlocal enabledelayedexpansion

set "filename=file.txt"

for /F "tokens=1,* delims==" %%a in ('findstr /i "username= password=" "%filename%"') do (
    if /I "%%a"=="username" (
        set "username=%%b"
        set "decoded_username="
        call :base64decode !username! decoded_username
    )

    if /I "%%a"=="password" (
        set "password=%%b"
        set "decoded_password="
        call :base64decode !password! decoded_password
        echo Username: !decoded_username!  Password: !decoded_password!
    )
)

endlocal
exit /b

:base64decode
setlocal
set "input=%~1"
set "decoded_output="
powershell -command "[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('%input%'))" >"%TEMP%\base64_output.txt"
set /p decoded_output=<"%TEMP%\base64_output.txt"
echo(%decoded_output%
endlocal & set "%~2=%decoded_output%"
exit /b
