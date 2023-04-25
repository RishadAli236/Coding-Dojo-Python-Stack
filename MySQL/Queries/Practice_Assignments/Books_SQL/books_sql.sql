SELECT * FROM users;
SELECT * FROM books;
SELECT * FROM favorites;

SET SQL_SAFE_UPDATES = 0;

INSERT INTO users (name)
VALUES ("Jane Amsden"), ("Emily Dixon"), ("Theodore Dostoevsky"), ("William Shapiro"), ("Lao Xiu");

INSERT INTO books (title, num_of_pages)
VALUES ("C Sharp", 250), ("Java", 900), ("Python", 500), ("PHP", 400), ("Ruby", 450);

UPDATE books
SET title = "C#"
WHERE id = 1;

UPDATE users
SET name = "Bill Sharpio"
where id = 4;

SELECT *
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id; 

INSERT INTO favorites (user_id, book_id)
VALUES (1, 1), (1, 2);

INSERT INTO favorites (user_id, book_id)
VALUES (2, 1), (2, 2), (2, 3);

INSERT INTO favorites (user_id, book_id)
VALUES (3, 1), (3, 2), (3, 3), (3, 4);

INSERT INTO favorites (user_id, book_id)
VALUES (4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

SELECT users.name, books.title
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id
WHERE book_id = 3;

SELECT users.id as user_id, users.name, books.id as book_id, books.title
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id
WHERE book_id = 3;

DELETE FROM favorites WHERE user_id = 2 and book_id = 3;

INSERT INTO favorites (user_id, book_id)
VALUES (5, 2);

SELECT books.title as 3rd_users_favorite_books
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id
WHERE user_id = 3;

SELECT users.name as users_that_favorited_5th_book
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id
WHERE book_id = 5;