-- Creating the user and grating usage to the database
CREATE USER 'crawler_user'@'%' IDENTIFIED BY 'daniella';

GRANT ALL PRIVILEGES ON periodic_table.* TO 'crawler_user'@'%';

FLUSH PRIVILEGES;

-- Creating the table in the database
CREATE TABLE IF NOT EXISTS periodic_elements (

    symbol TEXT,
    name TEXT,
    atomic_number INTEGER,
    atomic_mass FLOAT,
    chemical_group TEXT

);