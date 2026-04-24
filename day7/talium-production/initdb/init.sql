CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    condition VARCHAR(255) NOT NULL
);

INSERT INTO patients (name, condition) VALUES
('John Doe', 'Hypertension'),
('Jane Smith', 'Diabetes'),
('Michael Brown', 'Asthma');
