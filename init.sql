CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100)
);

CREATE TABLE scraped_data (

	id INT AUTO_INCREMENT PRIMARY KEY,
	deal_date DATE,
	security_code VARCHAR(10),
	security_name VARCHAR(255),
	client_name VARCHAR(255),
	deal_type VARCHAR(50),
	quantity INT,
	price DECIMAL(10, 2)
);
