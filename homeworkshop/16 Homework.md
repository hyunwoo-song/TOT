# 16 Homework

```sqlite
sqlite3 16homework.sqlite3

CREATE TABLE bands(id INTEGER PRIMARY KEY AUTOINCREMENT, 
	...>name TEXT NOT NULL,
    ...>location TEXT NOT NULL);
    
.headers on
.mode column
.schema 
----------
CREATE TABLE bands(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL,
location TEXT NOT NULL);
-----------

INSERT INTO bands (name, location)
	...>VALUES("Justin",'Seoul');
INSERT INTO bands (name, location)	
	...>VALUES("Simon",'New York');
INSERT INTO bands (name, location)	
	...>VALUES("Chang",'Las Vegas');
INSERT INTO bands (name, location)
	...>VALUES("John",'Sydney');
	
SELECT * FROM bands;
id          name        location  
----------  ----------  ----------
1           Justin      Seoul     
2           Simon       New York  
3           Chang       Las Vegas 
4           John        Sydney    


ALTER TABLE bands ADD COLUMN married INT;
SELECT * FROM bands;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      Seoul                 
2           Simon       New York              
3           Chang       Las Vegas             
4           John        Sydney      


UPDATE bands SET location='LA' WHERE id=1;
UPDATE bands SET married=1 WHERE id=1;
UPDATE bands SET married=0 WHERE id=2;
UPDATE bands SET married=0 WHERE id=3;
UPDATE bands SET married=1 WHERE id=4;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
2           Simon       New York    0         
3           Chang       Las Vegas   0         
4           John        Sydney      1       


DELETE FROM bands WHERE married=0;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
4           John        Sydney      1     


```

