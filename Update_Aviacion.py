import csv
import pyodbc
from dateutil import parser

# Conexión a la base de datos
def connect_to_db():
    connection = pyodbc.connect(
        '''DRIVER={ODBC Driver 17 for SQL Server};
        SERVER=DESKTOP-C48C4LP\\SQLEXPRESS;
        DATABASE=base_aviacion;
        Trusted_Connection=yes;'''
    )
    return connection

# Función para convertir fechas
def parse_date(date_str):
    try:
        if date_str == '\\N' or not date_str:
            return None  # Manejar valores no válidos como '\N'
        return parser.parse(date_str)
    except Exception as e:
        print(f"Error al convertir la fecha '{date_str}': {e}")
        return None

# Función para convertir valores numéricos
def parse_float_or_int(value):
    try:
        if value == '\\N' or not value:
            return None  # Manejar valores no válidos como '\N'
        if '.' in value:
            return float(value)  # Convertir a float si tiene punto decimal
        return int(value)  # Convertir a int si no tiene punto decimal
    except ValueError as e:
        print(f"Error al convertir el valor '{value}': {e}")
        return None

# Función para actualizar o insertar registros en aircraft_data
def merge_aircraft_data(cursor, row):
    query = '''
    MERGE INTO aircraft_data AS target
    USING (SELECT ? AS aircraft_code, ? AS model, ? AS range) AS source
    ON target.aircraft_code = source.aircraft_code
    WHEN MATCHED THEN 
        UPDATE SET model = source.model, range = source.range
    WHEN NOT MATCHED THEN
        INSERT (aircraft_code, model, range)
        VALUES (source.aircraft_code, source.model, source.range);
    '''
    cursor.execute(query, row['aircraft_code'], row['model'], parse_float_or_int(row['range']))

# Otras funciones para tablas como airports_data, bookings, etc.
# ...

def process_csv_and_update_db(csv_file):
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Actualizar aircraft_data
                if row['aircraft_code'] and row['model'] and row['range']:
                    merge_aircraft_data(cursor, row)

                # Añadir más funciones para actualizar las demás tablas...
        
        connection.commit()  # Confirmar los cambios
        print("Actualización de las tablas completada exitosamente.")
    except Exception as e:
        print(f"Error al actualizar las tablas: {e}")
        connection.rollback()  # Revertir cambios en caso de error
    finally:
        cursor.close()
        connection.close()  # Cerrar la conexión a la base de datos

# Ejecutar el script
if __name__ == '__main__':
    process_csv_and_update_db('archivo_combinado.csv')
