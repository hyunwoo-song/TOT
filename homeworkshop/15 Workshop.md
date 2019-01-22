#  15 Workshop

```sqlite
CREATE TABLE bands(id INTEGER PRIMARY KEY AUTOINCREMENT, 
	...>name TEXT NOT NULL,
    ...>debut INT NOT NULL);
    
    
INSERT INTO bands (name, debut)
	...>VALUES("Queen",1973);
INSERT INTO bands (name, debut)	
	...>VALUES("Coldplay",1998);
INSERT INTO bands (name, debut)	
	...>VALUES("MCR",2001);
	
	
.schema bands  
SELECT id, name FROM bands;
id          name      
----------  ----------
1           Queen     
2           Coldplay  
3           MCR     



SELECT name FROM bands WHERE debut<2000;

name      
----------
Queen     
Coldplay  
sqlite> 
    
```

