-- Create the user table

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

-- INSERT test records:

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES(
    "John", 
    "DOE",
    "Camping"
);
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES(
    "Jane", 
    "DOE",
    "Tennis"
);
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES(
    "Timmy", 
    "DOE",
    "Cooking"
);
