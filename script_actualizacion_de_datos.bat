@echo off

REM Ruta de Python (asegúrate de que el path es correcto)
set PYTHON_PATH=C:\Program Files\Python312

REM Ruta del script de Python
set SCRIPT_PATH=D:\Documentos\Todo henry\Proyecto integrador grupal\travel_sqlite\Automatizacion.py

REM Ejecutar el script de Python
%PYTHON_PATH% %SCRIPT_PATH%

REM Pausar para ver la salida
pause
