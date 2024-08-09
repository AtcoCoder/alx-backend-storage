-- creates users table


CREATE TABLE users (
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
)
