INSERT INTO parents (name) VALUES ('John'), ('Jane'), ('Bob');
INSERT INTO children (name, parent_id) VALUES ('Alice', 1), ('Eve', 2);


UPDATE parents p
SET has_children = false
WHERE NOT EXISTS (
    SELECT 1
    FROM children c
    WHERE c.parent_id = p.id
);


SELECT * FROM parents;