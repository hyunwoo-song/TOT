# 16 Workshop

```sqlite
sqlite3 16workshop.sqlite3

CREATE TABLE bands(id INTEGER PRIMARY KEY AUTOINCREMENT, 
	...>name TEXT NOT NULL,
    ...>debut INT NOT NULL);
    
.tables # 확인하는법   

INSERT INTO bands (name, debut)
	...>VALUES("Queen",1973);
INSERT INTO bands (name, debut)	
	...>VALUES("Coldplay",1998);
INSERT INTO bands (name, debut)	
	...>VALUES("MCR",2001);


# column  추가하는법
ALTER TABLE bands ADD COLUMN members INT;
SELECT * FROM bands;

# 이뿌게 보는법
.headers on
.mode column

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;

SELECT * FROM bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        9   

UPDATE bands SET members=5 WHERE id=3;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
3           MCR         2001        5      

DELETE FROM bands WHERE id=2;
SELECT * FROM bands;

id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
3           MCR         2001        9     
```



