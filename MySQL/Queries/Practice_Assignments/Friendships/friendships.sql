SELECT * FROM users;
SELECT * FROM friendships;
SELECT *
FROM users
JOIN friendships
ON users.id = friendships.user_id
JOIN users as users2
ON friendships.friend_id = users2.id;

INSERT INTO users (first_name, last_name)
VALUES ("Amy", "Giver"), ("Eli", "Byers"), ("Marky", "Mark"), ("Big", "Bird"), ("Kermit", "The Frog"), ("Cookie", "Monster");

INSERT INTO friendships (user_id, friend_id)
VALUES (1, 2), (1, 4), (1, 6);

INSERT INTO friendships (user_id, friend_id)
VALUES (2, 1), (2, 3), (2, 5);

INSERT INTO friendships (user_id, friend_id)
VALUES (3, 2), (3, 5);

INSERT INTO friendships (user_id, friend_id)
VALUES (4, 3);

INSERT INTO friendships (user_id, friend_id)
VALUES (5, 1), (5, 6);

INSERT INTO friendships (user_id, friend_id)
VALUES (6, 2), (6, 3);

SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as users2
ON friendships.friend_id = users2.id;

SELECT users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
JOIN users as users2
ON friendships.friend_id = users2.id
WHERE users.id = 1;

SELECT COUNT(id) as count_of_friendships
FROM friendships;

SELECT users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
JOIN users as users2
ON friendships.friend_id = users2.id
WHERE users.id = 3
ORDER BY friend_first_name, friend_last_name;



