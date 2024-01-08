@echo off
:menu
cls
echo -------------------------
echo  Python Service Menu
echo -------------------------
echo 1. Start Service
echo 2. Stop Service
echo 3. Restart Service
echo 4. Install Service
echo 5. Uninstall Service
echo 6. Run in Console
echo 7. Exit
echo -------------------------
set /p choice=Enter your choice (1-7): 

if "%choice%"=="1" goto start
if "%choice%"=="2" goto stop
if "%choice%"=="3" goto restart
if "%choice%"=="4" goto install
if "%choice%"=="5" goto uninstall
if "%choice%"=="6" goto console
if "%choice%"=="7" goto exit

:start
call Start_Service.bat
pause
goto menu

:stop
call Stop_Service.bat
pause
goto menu

:restart
call Restart_Service.bat
pause
goto menu

:install
call Install_Service.bat
pause
goto menu

:uninstall
call Uninstall_Service.bat
pause
goto menu

:console
call Run_Console.bat
pause
goto menu

:exit
echo Exiting...
exit
