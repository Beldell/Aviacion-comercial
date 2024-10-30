
import pyodbc
from datetime import datetime
import os

# Función para conectar a la base de datos
def connect_to_db():
    connection = pyodbc.connect(
        '''DRIVER={ODBC Driver 17 for SQL Server};
        SERVER=DESKTOP-C48C4LP\\SQLEXPRESS;
        DATABASE=base_aviacion;
        Trusted_Connection=yes;'''
    )
    return connection

# Función para realizar la copia de seguridad de la base de datos
def backup_database(cursor, database_name, backup_directory):
    # Crear el nombre del archivo de copia de seguridad con la fecha actual
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{backup_directory}\\{database_name}_backup_{current_time}.bak"

    # Comando SQL para hacer la copia de seguridad
    query = f'''
    BACKUP DATABASE {database_name}
    TO DISK = '{backup_filename}'
    WITH FORMAT,
         MEDIANAME = 'SQLServerBackups',
         NAME = 'Full Backup of {database_name}';
    '''
    
    cursor.execute(query)
    print(query)
    print(f"Copia de seguridad completada exitosamente. Archivo: {backup_filename}")

# Función principal que se encarga de la copia de seguridad
def main():
    # Definir el nombre de la base de datos y el directorio de backup
    database_name = 'base_aviacion'
    backup_directory = r'D:\Documentos\Todo henry\Proyectos de henry\travel'  # Cambia esto por la ruta donde quieras guardar el backup
    print(backup_directory)
    # Verificar que el directorio exista, si no, crearlo
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Conectar a la base de datos
    connection = connect_to_db()
    cursor = connection.cursor()

    # Ejecutar la copia de seguridad
    try:
        connection.autocommit = True
        backup_database(cursor, database_name, backup_directory)
        connection.commit()  # Confirmar la operación
    except Exception as e:
        print(f"Error realizando la copia de seguridad: {e}")
        connection.rollback()  # Revertir en caso de error
    finally:
        cursor.close()
        connection.close()  # Cerrar la conexión a la base de datos

# Ejecutar el script
if __name__ == '__main__':
    main()