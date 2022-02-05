.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
    FROM students as a, fa17students as b
    WHERE a.date = b.date and a.color = b.color
      and a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT seven FROM students as s, checkboxes as c
    WHERE s.time = c.time and s.number = 7 AND c."7" = "True";

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count FROM fa17students GROUP BY number
    ORDER BY count DESC
    LIMIT 1;


CREATE TABLE fa17favpets AS
    SELECT pet, COUNT(*) AS count FROM fa17students GROUP BY pet
    ORDER BY count DESC
    LIMIT 10;


CREATE TABLE sp18favpets AS
    SELECT pet, COUNT(*) AS count FROM students GROUP BY pet
    ORDER BY count DESC
    LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) AS COUNT FROM students WHERE pet = 'dog'
    GROUP BY pet;


CREATE TABLE sp18alldogs AS
  SELECT 'dog', COUNT(*) AS COUNT FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) AS count FROM students
    WHERE seven = '7'
    GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) FROM students GROUP BY smallest
    ORDER BY smallest;

