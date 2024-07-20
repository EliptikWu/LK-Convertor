@echo off
REM Establecer el título de la ventana
title LK Convertor

REM Mostrar el mensaje adicional
echo This is a converter to make presets for Oraxen and ItemsAdder.
echo Lk Industries Convertor v1.0
echo.

REM Cambiar al directorio donde se encuentra el script Python
cd /d %~dp0

REM Ejecutar el script Python
python LK_Convertor.py

REM Pausar para ver los resultados
pause
