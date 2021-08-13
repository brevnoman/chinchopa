create table people (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), surname VARCHAR(100));
ALTER TABLE people RENAME TO workers;
ALTER TABLE people ADD COLUMN salary INTEGER(32);
INSERT INTO workers (name, surname, salary) VALUES("Dodik", "Diskotechniy", 15)
INSERT INTO workers (name, surname, salary) VALUES("Alpha", "Chad", 300000000)
UPDATE workers SET salary=NULL WHERE name="Dodik"
UPDATE workers set salary= 999999999 WHERE name="Alpha"
DELETE FROM workers WHERE salary=NULL
