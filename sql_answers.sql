--Question 1---
SELECT ROUND(AVG(all_trips.trip_distance),3) AS avg_trip_distance
FROM (
    SELECT 2009_trips_table.trip_distance
    FROM 2009_trips_table
    WHERE passenger_count <= 2
    UNION ALL
    SELECT 2010_trips_table.trip_distance
    FROM 2010_trips_table
    WHERE passenger_count <= 2
    UNION ALL
    SELECT 2011_trips_table.trip_distance
    FROM 2011_trips_table
    WHERE passenger_count <= 2
    UNION ALL
    SELECT 2012_trips_table.trip_distance
    FROM 2012_trips_table
    WHERE passenger_count <= 2
) AS all_trips;

--Question 2--
SELECT name, SUM(all_trips.total_amount)
FROM (
    SELECT 2009_trips_table.total_amount, 2009_trips_table.vendor_id
    FROM 2009_trips_table
    UNION ALL
    SELECT 2010_trips_table.total_amount, 2010_trips_table.vendor_id
    FROM 2010_trips_table
    UNION ALL
    SELECT 2011_trips_table.total_amount, 2011_trips_table.vendor_id
    FROM 2011_trips_table
    UNION ALL
    SELECT 2012_trips_table.total_amount, 2012_trips_table.vendor_id
    FROM 2012_trips_table
) AS all_trips
INNER JOIN vendor_lookup
ON all_trips.vendor_id = vendor_lookup.vendor_id
GROUP BY name
ORDER BY all_trips.total_amount DESC
LIMIT 3;

--Question 3
SELECT TO_TIMESTAMP(pickup_datetime, 'YYYY-MM-DDTHH24:MI:SS.US+Z') AS pickup_datetime_converted, COUNT(pl.payment_lookup)
FROM (
    SELECT 2009_trips_table.pickup_datetime, 2009_trips_table.payment_type
    FROM 2009_trips_table
    UNION ALL
    SELECT 2010_trips_table.pickup_datetime, 2010_trips_table.payment_type
    FROM 2010_trips_table
    UNION ALL
    SELECT 2011_trips_table.pickup_datetime, 2011_trips_table.payment_type
    FROM 2011_trips_table
    UNION ALL
    SELECT 2012_trips_table.pickup_datetime, 2012_trips_table.payment_type
    FROM 2012_trips_table
) AS all_trips
INNER JOIN payment_lookup-csv AS pl
ON all_trips.payment_type = pl.payment_type
WHERE payment_lookup = 'Cash'
GROUP BY pickup_datetime_converted;
                                                                                  "Cash"