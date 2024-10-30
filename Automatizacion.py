# Actualizacion de Datos

import pyodbc
import csv
from datetime import datetime

# Función para conectarse a la base de datos
def connect_to_db():
    connection = pyodbc.connect(
        '''DRIVER={ODBC Driver 17 for SQL Server};
        SERVER=DESKTOP-C48C4LP\\SQLEXPRESS;
        DATABASE=base_aviacion;
        Trusted_Connection=yes;'''
    )
    return connection

# Función para actualizar el estado del vuelo
def update_flight_status(cursor, flight_id, new_status, actual_departure=None, actual_arrival=None):
    query = '''
    UPDATE flights 
    SET status = ?, actual_departure = ?, actual_arrival = ?
    WHERE flight_id = ?
    '''
    cursor.execute(query, (new_status, actual_departure, actual_arrival, flight_id))

# Función para procesar el archivo CSV y actualizar los datos en la base de datos
def process_csv_and_update_db(csv_file):
    # Conectar a la base de datos
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                flight_id = int(row['flight_id'])
                new_status = row['new_status']
                
                # Convertir las fechas a formato datetime si están presentes
                actual_departure = None if not row['actual_departure'] else datetime.strptime(row['actual_departure'], '%Y-%m-%d %H:%M:%S')
                actual_arrival = None if not row['actual_arrival'] else datetime.strptime(row['actual_arrival'], '%Y-%m-%d %H:%M:%S')

                # Actualizar los datos del vuelo en la base de datos
                update_flight_status(cursor, flight_id, new_status, actual_departure, actual_arrival)

        connection.commit()  # Confirmar los cambios
        print("Actualización de vuelos completada exitosamente.")
    except Exception as e:
        print(f"Error actualizando los vuelos: {e}")
        connection.rollback()  # Revertir cambios en caso de error
    finally:
        cursor.close()
        connection.close()  # Cerrar la conexión a la base de datos

# Ejecutar el script
if __name__ == '__main__':
    csv_file = 'flights_update.csv'  # Nombre del archivo CSV
    process_csv_and_update_db(csv_file)
