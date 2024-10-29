:: @ECHO OFF

::CHCP 65001 > null
:: Mensaje de inicio
::ECHO Iniciando el script de automatización...

:: Activar el entorno de Anaconda
::ECHO Activando el entorno de Anaconda...
::call C:\ProgramData\anaconda3\Scripts\activate.bat
:: Cambiar al directorio donde está el script
::ECHO Navegando al directorio de trabajo...
::cd "D:\Documentos\Todo henry\Proyecto integrador grupal\travel_sqlite"
:: Verificar si el directorio es correcto
::ECHO Directorio actual: %CD%

:: Ejecutar el script Python
::ECHO Ejecutando el script Python...
::python Automatizacion.py

:: Mensaje de finalización del script Python
::ECHO El script Python ha finalizado.

::PAUSE

@echo off
REM Cambiar a la ruta del directorio del script de Python
cd /d "D:\Documentos\Todo henry\Proyecto integrador grupal\travel_sqlite"

ECHO Ejecutando el script Python...
REM Ejecutar el script de Python
python Automatizacion.py
ECHO El script Python ha finalizado.

PAUSE