@echo off
setlocal enabledelayedexpansion

set "jarFile=path\to\your\jar\file.jar"
set "outputDir=path\to\your\output\directory"

set "jarFileName=%~n1"
set "jarFileExtension=%~x1"

mkdir "%outputDir%"

echo Extracting classes from %jarFile%...
mkdir "%outputDir%\%jarFileName%_classes"
jd-gui.exe -e "%jarFile%" "%outputDir%\%jarFileName%_classes"
echo.

echo Creating new jar file...
cd "%outputDir%\%jarFileName%_classes"
jar cvf "%outputDir%\%jarFileName%_extracted%jarFileExtension%" .
cd "%~dp0"
echo Extraction complete.
