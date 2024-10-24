::@echo off

::REM Ruta de Python (asegúrate de que el path es correcto)
::set PYTHON_PATH=C:\Program Files\Python312\python.exe

::REM Ruta del script de Python
::set SCRIPT_PATH=D:\Documentos\Todo henry\Proyecto integrador grupal\travel_sqlite\Update_Aviacion.py

::REM Ejecutar el script de Python
::%PYTHON_PATH% %SCRIPT_PATH%

::REM Pausar para ver la salida
::pause

@echo off
REM Cambiar a la ruta del directorio del script de Python
cd /d "D:\Documentos\Todo henry\Proyecto integrador grupal\travel_sqlite"

ECHO Ejecutando el script Python...
REM Ejecutar el script de Python
python Update_Aviacion.py
ECHO El script Python ha finalizado.

PAUSE