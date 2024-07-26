-- creates a table second_table in the database add multiples rows.
CREATE TABLE
	IF NOT EXISTS second_table (
		id INT,
		name VARCHAR(256),
		score INT,
		PRIMARY KEY (id)
	);

INSERT INTO 
	second_table (id, name, score)
VALUES 
		(1, 'John', 10),
		(2, 'Alex', 3),
		(3, 'Bob', 7),
		(4, 'George', 8);
