:: ========================================================
:: generate_ui.bat - PyQt5 UI Compiler Script
::
:: PURPOSE:
:: 1. Compiles Qt resource files (.qrc → _rc.py)
:: 2. Converts Qt Designer files (.ui → .py)
:: 3. Fixes resource import paths in generated files
:: Automatically updates all UI and resource files when design changes occur
::
:: TO RUN:
:: Type .\generate_ui.bat in VSCode terminal or CMD
:: 
:: TO DELETE:
:: del ui\generated_files\*.py
:: del ui\resources\jj_resources_rc.py
:: ========================================================

@echo off
cd /d "C:\Users\jhane\Desktop\New folder>"

:: Check if required commands exist
where pyuic5 >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pyuic5 not found. Make sure PyQt5 is installed.
    pause
    exit /b 1
)

where pyrcc5 >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pyrcc5 not found. Make sure PyQt5 is installed.
    pause
    exit /b 1
)

:: Clear old generated files
del /q gui_classes\*.py >nul 2>&1
del /q resources\jj_resources_rc.py >nul 2>&1

:: Compile resources FIRST
echo Compiling resources...
pushd resources
pyrcc5 jj_resources.qrc -o jj_resources_rc.py
if %errorlevel% neq 0 (
    echo Error compiling resources!
    popd
    pause
    exit /b 1
)
popd

:: Convert UI files
echo Generating UI files...

:: Authentication pages
call :convert_ui UI_Landing
call :convert_ui UI_LogIn
call :convert_ui UI_ForgotPass

:: Owner interface
call :convert_ui UI_ODashboard
call :convert_ui UI_OInventory
call :convert_ui UI_OOrders
call :convert_ui UI_OSales
call :convert_ui UI_OStockHistory
call :convert_ui UI_OAccount

:: Cashier interface
call :convert_ui UI_CDashboard
call :convert_ui UI_COrders
call :convert_ui UI_CSales
call :convert_ui UI_CAccount
call :convert_ui UI_COrder_History

:: ========================================================
:: VERIFY ALL GENERATED CLASS NAMES
:: ========================================================
echo.
echo Verifying all UI class names...
echo.

:: Authentication pages
findstr "class Ui_" gui_classes\UI_Landing.py
findstr "class Ui_" gui_classes\UI_LogIn.py
findstr "class Ui_" gui_classes\UI_ForgotPass.py

:: Owner interface
findstr "class Ui_" gui_classes\UI_ODashboard.py
findstr "class Ui_" gui_classes\UI_OInventory.py
findstr "class Ui_" gui_classes\UI_OOrders.py
findstr "class Ui_" gui_classes\UI_OSales.py
findstr "class Ui_" gui_classes\UI_OStockHistory.py
findstr "class Ui_" gui_classes\UI_OAccount.py

:: Cashier interface
findstr "class Ui_" gui_classes\UI_CDashboard.py
findstr "class Ui_" gui_classes\UI_COrders.py
findstr "class Ui_" gui_classes\UI_CSales.py
findstr "class Ui_" gui_classes\UI_CAccount.py
findstr "class Ui_" gui_classes\UI_COrder_History.py

echo.
echo Class name verification complete!
pause

:: Fix imports in all generated files
echo Fixing imports...
powershell -Command "(Get-ChildItem ui/generated_files/*.py) | ForEach-Object { (Get-Content $_) -replace 'import jj_resources_rc', 'from ui.resources import jj_resources_rc' | Set-Content $_ }"

:: Verify generation - more accurate check
set "error=0"
for /f %%i in ('dir /b gui_classes ^| find /c /v ""') do set "filecount=%%i"
if %filecount% lss 15 (
    set "error=1"
    echo Warning: Expected 15 files but only found %filecount%!
)

if %error% equ 0 (
    echo Success: All UI files and resources generated correctly!
    echo Total files generated: %filecount%
) else (
    echo Warning: Some UI files might be missing!
)

pause
exit /b 0

:convert_ui
pyuic5 views/%1.ui -o gui_classes/%1.py
if not exist "gui_classes/%1.py" (
    echo Error generating %1.py
    set "error=1"
)
exit /b