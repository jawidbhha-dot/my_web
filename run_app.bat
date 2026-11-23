@echo off
title OptiScan AI Launcher
cd /d "%~dp0"
python app.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Opening in default browser instead...
    start index.html
)
