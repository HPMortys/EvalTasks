CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
     username VARCHAR(50) NOT NULL UNIQUE,
     email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO users (username, email) VALUES
            ('bob_jones', 'bob@example.com'),
            ('mary_davis', 'mary@example.com'),
            ('david_wilson', 'david@example.com'),
            ('susan_thompson', 'susan@example.com'),
            ('michael_smith', 'michael@example.com'),
            ('lisa_anderson', 'lisa@example.com'),
            ('kevin_miller', 'kevin@example.com'),
            ('jennifer_brown', 'jennifer@example.com'),
            ('steven_jackson', 'steven@example.com'),
            ('amanda_taylor', 'amanda@example.com');
