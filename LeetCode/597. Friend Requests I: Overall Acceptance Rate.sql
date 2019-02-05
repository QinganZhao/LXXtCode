SELECT ROUND(IFNULL((COUNT(DISTINCT requester_id, accepter_id)) /
(SELECT COUNT(DISTINCT sender_id, send_to_id) FROM friend_request), 0), 2) accept_rate
FROM request_accepted
