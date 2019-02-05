SELECT f1.follower, COUNT(DISTINCT f2.follower) num
FROM follow f1
JOIN follow f2 ON f1.follower = f2.followee
GROUP BY f1.follower
