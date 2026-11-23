@echo off
rem ============================================================================================================
rem  Voxel Fauna - render. Double-click it. (Ported from Nilant's render.bat, 2026-11-16.)
rem
rem  Builds every animal's .blend from its model.py, renders LOW previews, and the ULTRA renders of every
rem  approved animal (the two master renders and the frames of the looped animation), offline: no internet, no
rem  Claude. Rendering, then P packages the GIF, the cards and the stock JPEG.
rem  The menu runs from ..\scripts\render_cli.py (a cover, then boxes). EVERY step asks the same two things:
rem    WHICH animals   the ones that still need it, all of them, or your own list (numbers, ranges, codes, names)
rem    WHAT            checkboxes: for Package the loop GIF, either card, the stock JPEG and CSVs, the Gumroad zip, the
rem                    registry (presets: full, stock only, PDF only, GIF only, Gumroad bundle); for the renders the
rem                    masters and the loop; force, LOW, rigs at once, shut the PC down when it finishes
rem    RENDER   1 build .blend . 2 LOW previews + rigs + loops . 3 ULTRA masters + loop . P package . R rig + loops
rem    CHECK    5 status of every animal . 6 one animal's files        MORE   4 one animal, any step . Q quit
rem  Your choices are remembered in render_options.json beside this file (git-ignored).
rem  Pause any time: Ctrl+C or close the window (finished images are kept); open it again and choose the same option.
rem  Without the menu: render.bat status | files <code> | build | preview | final | package | rig   [animals] [options]
rem    e.g.  render.bat package 000001-000010 --preset stock       render.bat final all --parts dyn,block --shutdown
rem          render.bat package --parts gif,card_en              (no animals = the ones that still need it)
rem    render.bat <command> --help lists every option.
rem  Blender: the first blender.exe found below is remembered in ..\blender_path.txt (delete it to choose again).
rem  Python: remembered in python_path.txt beside this file (delete it to choose again).
rem  Animals: the 02 Animals folder is read from animal_path.txt beside this file; if it is missing and 02 Animals is not
rem  found beside the scripts, the window asks for the folder's path and remembers it (delete the file to choose again).
rem  Guide: "Voxel Fauna - How to Render.md" in this folder.
rem ============================================================================================================
setlocal EnableExtensions
title Voxel Fauna - render
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
cd /d "%~dp0"
mode con: cols=100 lines=46 >nul 2>&1
for /f %%e in ('echo prompt $E^| cmd') do set "ESC=%%e"
set "OK=%ESC%[92m"
set "BAD=%ESC%[91m"
set "DIM=%ESC%[90m"
set "BLD=%ESC%[1m"
set "ORG=%ESC%[38;5;208m"
set "AMB=%ESC%[38;5;214m"
set "TEAL=%ESC%[38;5;43m"
set "END=%ESC%[0m"

cls
echo.
echo    %AMB%     +---------+%END%
echo    %AMB%    /         /^|%END%       %BLD%V O X E L   F A U N A%END%
echo    %ORG%   /         / ^|%END%       %DIM%render studio  -  isometric voxel animals%END%
echo    %ORG%  +---------+  ^|%END%       %DIM%built, rigged and animated in Blender%END%
echo    %TEAL%  ^|         ^|  +%END%       %DIM%offline  -  nothing leaves this PC%END%
echo    %TEAL%  ^|         ^| /%END%        %DIM%a Nilant side collection  -  powered by ihdyo%END%
echo    %TEAL%  ^|         ^|/%END%
echo    %TEAL%  +---------+%END%
echo.
echo  %DIM%------------------------------------------------------------------------------------------%END%
echo.

if not exist "..\scripts\render_cli.py" (
  echo  %BAD%[ !! ]%END% The render scripts are missing ^(..\scripts\render_cli.py^).
  echo.
  pause
  exit /b 1
)
echo  %OK%[ OK ]%END% Render scripts   %DIM%..\scripts\render_cli.py%END%

rem ---- find Blender (same order as Nilant) -------------------------------------------------------------------
set "B="
if exist "..\blender_path.txt" set /p B=<"..\blender_path.txt"
if defined B if not exist "%B%" set "B="
if not defined B if defined BLENDER if exist "%BLENDER%" set "B=%BLENDER%"
if not defined B for /d %%D in ("%LOCALAPPDATA%\Programs\Blender*") do if exist "%%~D\blender.exe" set "B=%%~D\blender.exe"
if not defined B for /d %%D in ("%LOCALAPPDATA%\Programs\Blender*") do for /d %%E in ("%%~D\*") do if exist "%%~E\blender.exe" set "B=%%~E\blender.exe"
if not defined B for /d %%D in ("%ProgramFiles%\Blender Foundation\Blender*") do if exist "%%~D\blender.exe" set "B=%%~D\blender.exe"
if not defined B for /f "delims=" %%F in ('where blender.exe 2^>nul') do if not defined B set "B=%%F"
if defined B goto have_blender
echo  %BAD%[ !! ]%END% Blender was not found. Drag blender.exe onto this window and press Enter.
echo         %DIM%The Microsoft Store Blender cannot run in a console: use a regular install or the portable zip.%END%
set /p B=  blender.exe:
:have_blender
set "B=%B:"=%"
if exist "%B%" goto blender_ok
echo  %BAD%[ !! ]%END% Not found: %B%
pause
exit /b 1
:blender_ok
> "..\blender_path.txt" echo %B%
echo  %OK%[ OK ]%END% Blender          %DIM%%B%%END%

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
if defined Q goto python_without_packages
echo  %BAD%[ !! ]%END% No Python was found. Install Python 3.10+ from python.org ^(tick "Add python.exe to PATH"^), then run this again.
pause
exit /b 1
:python_without_packages
echo  %BAD%[ !! ]%END% Pillow, openpyxl and PyMuPDF are missing for %Q%
echo         %DIM%They lay the information cards and the registry. One-time download; renders stay offline.%END%
set "YN="
set /p YN=  Install them now? [Y/N]:
if /i not "%YN%"=="Y" goto no_install
"%Q%" -m pip install --user pillow openpyxl pymupdf
"%Q%" -c "import PIL, openpyxl, fitz" >nul 2>&1 && set "P=%Q%"
if defined P goto have_python
echo.
echo  %BAD%[ !! ]%END% The install did not work ^(see above^).
pause
exit /b 1
:no_install
echo  %DIM%Then run: "%Q%" -m pip install pillow openpyxl pymupdf   and open this again.%END%
pause
exit /b 1
:have_python
> "python_path.txt" echo %P%
echo  %OK%[ OK ]%END% Python           %DIM%%P%%END%

rem ---- find the animals (the 02 Animals folder) --------------------------------------------------------------------
rem  1. animal_path.txt beside this file (this PC's path, written below)   2. ..\..\..\02 Animals, the folder beside the
rem  scripts   3. otherwise ask: paste the path of the 02 Animals folder and it is remembered in animal_path.txt.
set "A="
if exist "animal_path.txt" set /p A=<"animal_path.txt"
if defined A set "A=%A:"=%"
if defined A if not exist "%A%\" set "A="
if not defined A for %%I in ("%~dp0..\..\..\02 Animals") do if exist "%%~fI\" set "A=%%~fI"
if defined A goto have_animals
echo  %BAD%[ !! ]%END% The 02 Animals folder was not found next to the scripts.
echo         %DIM%Open it in Explorer, copy its address ^(the folder holding the 000001 ... folders^), paste it here.%END%
set "TRIES=0"
:ask_animals
set /a TRIES+=1
if %TRIES% gtr 5 (
  echo  %BAD%[ !! ]%END% No folder given. Create animal_path.txt beside this file with the path of 02 Animals in it.
  pause
  exit /b 1
)
set "A="
set /p A=  Path of 02 Animals:
if not defined A goto ask_animals
set "A=%A:"=%"
if not exist "%A%\" (
  echo  %BAD%Not a folder:%END% %A%
  goto ask_animals
)
set "ANY="
for /d %%D in ("%A%\0*" "%A%\1*" "%A%\2*" "%A%\3*") do set "ANY=1"
if not defined ANY (
  echo  %BAD%No animal folders ^(like 000001 ...^) in:%END% %A%
  goto ask_animals
)
:have_animals
> "animal_path.txt" echo %A%
set "VF_ANIMALS=%A%"
echo  %OK%[ OK ]%END% Animals          %DIM%%A%%END%

rem ---- run ----------------------------------------------------------------------------------------------------
set "BLENDER=%B%"
echo.
echo  %DIM%------------------------------------------------------------------------------------------%END%
echo  %ORG%Starting the render menu...%END%
if "%~1"=="" ping -n 2 127.0.0.1 >nul
"%P%" -X utf8 "%~dp0..\scripts\render_cli.py" %*
if errorlevel 1 (
  echo.
  echo  %BAD%[ !! ]%END% Stopped with an error ^(see above^).
  pause
  exit /b 1
)
if not "%~1"=="" pause
echo.
echo  %TEAL%Bye. Finished work is kept: open this again and choose the same step.%END%
endlocal
