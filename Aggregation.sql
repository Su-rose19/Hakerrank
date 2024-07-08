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
