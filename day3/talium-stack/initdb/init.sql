CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    condition VARCHAR(100)
);

INSERT INTO patients (name, condition) VALUES
    ('John Adeyemi', 'Diabetes'),
    ('Mary Okafor', 'Hypertension'),
    ('Tovia Rapheal', 'Asthma');
