--uso de la base de datos--
USE base_aviacion;

-----------------------------------------------------------------------------------------------------------------------------

--consultas simples--

--Vuelos con M�s Tickets Vendidos (TOP 5)--
SELECT TOP 5
    f.flight_id,
    f.aircraft_code,
    f.departure_airport AS origin,
    f.arrival_airport AS destination,
    COUNT(tf.ticket_no) AS tickets_sold
FROM 
    flights f
INNER JOIN dbo.ticket_flights tf ON f.flight_id = tf.flight_id
GROUP BY 
    f.flight_id, f.aircraft_code, f.departure_airport, f.arrival_airport
ORDER BY 
    tickets_sold DESC;


--Vuelos con Menos Tickets Vendidos --

SELECT TOP 5
    f.flight_id,
    f.aircraft_code,
    f.departure_airport AS origin,
    f.arrival_airport AS destination,
    COUNT(tf.ticket_no) AS tickets_sold  -- Contar el n�mero de tickets vendidos
FROM 
    flights f
LEFT JOIN ticket_flights tf ON f.flight_id = tf.flight_id  -- Relacionar vuelos con tickets
GROUP BY 
    f.flight_id, f.aircraft_code, f.departure_airport, f.arrival_airport
ORDER BY 
    tickets_sold DESC;  -- Ordenar de menor a mayor

--Total de tickets vendidos por aeropuerto de origen --

--Ver qu� aeropuertos han generado m�s ventas de tickets, ordenados de mayor a menor--
SELECT f.departure_airport, COUNT(tf.ticket_no) AS total_tickets_sold
FROM flights f
LEFT JOIN ticket_flights tf ON f.flight_id = tf.flight_id
GROUP BY f.departure_airport
ORDER BY total_tickets_sold DESC;


--Total de tickets vendidos por avi�n--

SELECT f.aircraft_code, COUNT(tf.ticket_no) AS total_tickets_sold
FROM flights f
LEFT JOIN ticket_flights tf ON f.flight_id = tf.flight_id
GROUP BY f.aircraft_code
ORDER BY total_tickets_sold DESC;

--N�mero de vuelos por aeropuerto de origen--
--Muestra qu� aeropuertos tienen m�s salidas de vuelos--

SELECT f.departure_airport, COUNT(f.flight_id) AS total_flights
FROM flights f
GROUP BY f.departure_airport
ORDER BY total_flights DESC;

--Total de tickets vendidos por ruta (aeropuerto de origen a destino)--
--visi�n clara de las rutas m�s populares en cuanto a venta de tickets--
SELECT TOP 5 f.departure_airport, f.arrival_airport, COUNT(tf.ticket_no) AS total_tickets_sold
FROM flights f
LEFT JOIN ticket_flights tf ON f.flight_id = tf.flight_id
GROUP BY f.departure_airport, f.arrival_airport
ORDER BY total_tickets_sold DESC;





