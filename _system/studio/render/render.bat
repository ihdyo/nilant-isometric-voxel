@echo off
rem ============================================================================================================
rem  Voxel Fauna - render. Double-click it. (Ported from Nilant's render.bat, 2026-11-16.)
rem
rem  Builds every animal's .blend from its model.py, renders LOW previews, and the ULTRA renders of every
rem  approved animal (the two master renders and the frames of the looped animation), offline: no internet, no
rem  Claude. Rendering, then P packages the stock image, the GIF and the cards.
rem  The colour-coded menu runs from ..\scripts\render_cli.py:
rem    RENDER   1 build missing or stale .blend . 2 LOW previews of every built animal
rem             3 ULTRA renders (two masters + the loop) of every preview-approved animal . 4 one animal
rem             P package: stock image, loop GIF, A5 cards, stock files, zip, registry (offline, after 3)
rem    CHECK    5 status of every animal . 6 one animal's files
rem    CONTROL  Q quit
rem  Pause any time: Ctrl+C or close the window (finished images are kept); open it again and choose the same option.
rem  Without the menu: render.bat status | build | preview | final | package [code] | <code> [preview|final]
rem  Blender: the first blender.exe found below is remembered in ..\blender_path.txt (delete it to choose again).
rem  Python: remembered in python_path.txt beside this file (delete it to choose again).
rem  Guide: "Voxel Fauna - How to Render.md" in this folder.
rem ============================================================================================================
setlocal
title Voxel Fauna - render
chcp 65001 >nul
cd /d "%~dp0"
for /f %%e in ('echo prompt $E^| cmd') do set "ESC=%%e"
set "OK=%ESC%[92m"
set "BAD=%ESC%[91m"
set "DIM=%ESC%[90m"
set "END=%ESC%[0m"

if not exist "..\scripts\render_cli.py" (
  echo.
  echo  %BAD%The render scripts are missing ^(..\scripts\render_cli.py^).%END%
  echo.
  pause
  exit /b 1
)

rem ---- find Blender (same order as Nilant) -------------------------------------------------------------------
set "B="
if exist "..\blender_path.txt" set /p B=<"..\blender_path.txt"
if defined B if not exist "%B%" set "B="
if not defined B if defined BLENDER if exist "%BLENDER%" set "B=%BLENDER%"
if not defined B for /d %%D in ("%LOCALAPPDATA%\Programs\Blender*") do if exist "%%~D\blender.exe" set "B=%%~D\blender.exe"
if not defined B for /d %%D in ("%LOCALAPPDATA%\Programs\Blender*") do for /d %%E in ("%%~D\*") do if exist "%%~E\blender.exe" set "B=%%~E\blender.exe"
if not defined B for /d %%D in ("%ProgramFiles%\Blender Foundation\Blender*") do if exist "%%~D\blender.exe" set "B=%%~D\blender.exe"
if not defined B for /f "delims=" %%F in ('where blender.exe 2^>nul') do if not defined B set "B=%%F"
if not defined B (
  echo.
  echo  %BAD%Blender was not found.%END% Drag blender.exe onto this window and press Enter.
  echo  %DIM%The Microsoft Store Blender cannot run in a console: use a regular install or the portable zip.%END%
  set /p B=  blender.exe:
)
set "B=%B:"=%"
if not exist "%B%" (
  echo  %BAD%Not found:%END% %B%
  pause
  exit /b 1
)
> "..\blender_path.txt" echo %B%

rem ---- find Python with Pillow, openpyxl and PyMuPDF ------------------------------------------------------------------
set "P="
if exist "python_path.txt" set /p P=<"python_path.txt"
if defined P if not exist "%P%" set "P="
if defined P ("%P%" -c "import PIL, openpyxl, fitz" >nul 2>&1 || set "P=")
if not defined P for /f "delims=" %%F in ('where python.exe 2^>nul') do if not defined P (
  "%%F" -c "import PIL, openpyxl, fitz" >nul 2>&1 && set "P=%%F"
)
if not defined P for %%V in (3.12 3.13 3.11 3.10) do if not defined P (
  for /f "delims=" %%F in ('py -%%V -c "import sys, PIL, openpyxl, fitz; print(sys.executable)" 2^>nul') do set "P=%%F"
)
if defined P goto have_python
set "Q="
for /f "delims=" %%F in ('where python.exe 2^>nul') do if not defined Q echo %%F| findstr /i /c:"\WindowsApps\" >nul || if not defined Q "%%F" -c "import sys" >nul 2>&1 && set "Q=%%F"
if not defined Q for /f "delims=" %%F in ('py -3 -c "import sys; print(sys.executable)" 2^>nul') do set "Q=%%F"
if not defined Q (
  echo.
  echo  %BAD%No Python was found.%END% Install Python 3.10+ from python.org ^(tick "Add python.exe to PATH"^), then run this again.
  pause
  exit /b 1
)
echo.
echo  %BAD%Pillow, openpyxl and PyMuPDF are missing%END% for %Q%
echo  %DIM%They lay the information cards and the registry. One-time download; renders stay offline.%END%
set "YN="
set /p YN=  Install them now? [Y/N]: 
if /i not "%YN%"=="Y" goto no_install
"%Q%" -m pip install --user pillow openpyxl pymupdf
"%Q%" -c "import PIL, openpyxl, fitz" >nul 2>&1 && set "P=%Q%"
if defined P goto have_python
echo.
echo  %BAD%The install did not work ^(see above^).%END%
pause
exit /b 1
:no_install
echo  %DIM%Then run: "%Q%" -m pip install pillow openpyxl pymupdf   and open this again.%END%
pause
exit /b 1
:have_python
> "python_path.txt" echo %P%

rem ---- run ----------------------------------------------------------------------------------------------------
set "BLENDER=%B%"
echo  %DIM%Starting Voxel Fauna render...%END%
"%P%" "%~dp0..\scripts\render_cli.py" %*
if errorlevel 1 (
  echo.
  echo  %BAD%Stopped with an error ^(see above^).%END%
  pause
  exit /b 1
)
if not "%~1"=="" pause
endlocal
