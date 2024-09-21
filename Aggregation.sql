## Revising Aggregations - The SumFunction
SELECT SUM(POPULATION) FROM CITY
WHERE DISTRICT = 'California';

# -------------------------------------------
## Revising Aggregations - The CountFunction
SELECT COUNT(NAME) FROM CITY
WHERE POPULATION > 100000;

# -------------------------------------------
## Revising Aggregations - Averages
SELECT AVG(POPULATION) FROM CITY
WHERE DISTRICT = 'California';

# -------------------------------------------
## Average Population
SELECT FLOOR(AVG(POPULATION)) FROM CITY;

# -------------------------------------------
## Japan Population
SELECT SUM(POPULATION) FROM CITY
WHERE COUNTRYCODE = 'JPN';

# -------------------------------------------
## Population Density Difference
SELECT (MAX(POPULATION) - MIN(POPULATION))
FROM CITY;

# -------------------------------------------
## Weather Observation Station_2
SELECT CONVERT(SUM(LAT_N), DECIMAL(65,2)), CONVERT(SUM(LONG_W), DECIMAL(65,2)) 
FROM STATION;

# -------------------------------------------
## Weather Observation Station_16 
SELECT CONVERT((LAT_N), DECIMAL(65,4)) 
FROM STATION
WHERE LAT_N = ( SELECT MIN(LAT_N) 
               FROM STATION
               WHERE LAT_N> 38.7780);

# -------------------------------------------
## Weather Observation Station_17
SELECT CONVERT((LONG_W), DECIMAL(65,4)) 
FROM STATION
WHERE LAT_N = ( SELECT MIN(LAT_N) 
               FROM STATION
               WHERE LAT_N> 38.7780);

# -------------------------------------------
## Weather Observation Station 
