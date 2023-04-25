SELECT first_name, tweet
FROM users
LEFT JOIN faves ON users.id = faves.user_id
LEFT JOIN tweets ON faves.tweet_id = tweets.id
WHERE users.id = 2;

SELECT * 
FROM tweets
LEFT JOIN faves ON tweets.id = faves.tweet_id
WHERE faves.user_id = 2;

SELECT first_name, tweet
FROM users
LEFT JOIN faves ON users.id = faves.user_id
LEFT JOIN tweets ON faves.tweet_id = tweets.id
WHERE users.id = 2 OR users.id = 1;

SELECT followed_users.first_name, followers.first_name
FROM users AS followed_users
LEFT JOIN follows ON followed_users.id = follows.followed_id
LEFT JOIN users AS followers ON followers.id = follows.follower_id
WHERE followed_users.id = 1;

SELECT * 
FROM users
WHERE users.id NOT IN (
SELECT follower_id
FROM follows
WHERE followed_id = 2)
AND users.id != 2;

SELECT users.id, first_name, COUNT(follows.followed_id) AS follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
GROUP BY users.id;

SELECT users.id, first_name, COUNT(follower_id) AS follow_count
FROM users
LEFT JOIN follows
ON users.id = follows.follower_id
GROUP BY users.id;

SELECT * FROM follows




