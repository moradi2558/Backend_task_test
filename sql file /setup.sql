CREATE DATABASE family;


CREATE TABLE parents (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(255) NOT NULL,
    has_children BOOLEAN DEFAULT false 
);

CREATE TABLE children (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(255) NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES parents(id)
);
