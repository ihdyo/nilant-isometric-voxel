@echo off
rem ============================================================================================================
rem  Voxel Fauna - package. Double-click it after render.bat. (Owner, 2026-11-17.)
rem
rem  Builds the export package of every animal whose renders are done, offline: no Blender, no internet, no Claude.
rem  From the two master renders and the loop frames that render.bat made, for each animal:
rem    VF-<code>-STOCK-1x1.png   the 1:1 stock image, the centre square of the dynamic master
rem    VF-<code>-LOOP.gif        the looped dynamic animation, 1080 square
rem    VF-<code>-CARD-EN.pdf     the A5 card in English (front: the dynamic model over the photo with the info;
rem    VF-<code>-CARD-ID.pdf     the same in Bahasa Indonesia            back: the blocky model, "powered by ihdyo")
rem  then the stock JPEG and upload CSVs, the Gumroad zip and the registry rows.
rem  Without arguments: every rendered animal. With a code: that animal only (package.bat 26-001).
rem  Python: remembered in python_path.txt beside this file (needs Pillow, openpyxl and PyMuPDF).
rem  Guide: "Voxel Fauna - How to Render.md" in this folder.
rem ============================================================================================================
setlocal
title Voxel Fauna - package
chcp 65001 >nul
cd /d "%~dp0"
for /f %%e in ('echo prompt $E^| cmd') do set "ESC=%%e"
set "OK=%ESC%[92m"
set "BAD=%ESC%[91m"
set "DIM=%ESC%[90m"
set "END=%ESC%[0m"

rem ---- find Python with Pillow, openpyxl and PyMuPDF ----------------------------------------------------------
set "P="
if exist "python_path.txt" set /p P=<"python_path.txt"
if defined P if not exist "%P%" set "P="
if defined P "%P%" -c "import PIL, openpyxl, fitz" >nul 2>&1 || set "P="
if not defined P for /f "delims=" %%F in ('where python.exe 2^>nul') do if not defined P (
  "%%F" -c "import PIL, openpyxl, fitz" >nul 2>&1 && set "P=%%F"
)
if not defined P for %%V in (3.12 3.13 3.11 3.10) do if not defined P (
  for /f "delims=" %%F in ('py -%%V -c "import sys, PIL, openpyxl, fitz; print(sys.executable)" 2^>nul') do set "P=%%F"
)
if not defined P (
  echo.
  echo  %BAD%No Python with Pillow, openpyxl and PyMuPDF was found.%END%
  echo  %DIM%Install Python 3.10+ from python.org, then in a terminal: pip install pillow openpyxl pymupdf%END%
  pause
  exit /b 1
)
> "python_path.txt" echo %P%

rem ---- run ----------------------------------------------------------------------------------------------------
echo.
echo  %OK%Voxel Fauna - package%END%  %DIM%(stock crop, loop GIF, A5 cards in English and Indonesian, stock files,
echo  Gumroad zip, registry)%END%
echo.
if "%~1"=="" (
  "%P%" "%~dp0..\scripts\vf.py" package-all
) else (
  "%P%" "%~dp0..\scripts\vf.py" package %1
)
echo.
pause
