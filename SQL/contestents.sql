/*
You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.
*/

-- SELECT h.hacker_id, h.name, subs.total_score
-- from Hackers h join 
-- (SELECT tab2.hacker_id,SUM(tab2.max_score) as total_score
-- FROM (
-- Select * from (
-- SELECT hacker_id,challenge_id, max(score) as max_score
-- FROM Submissions
-- group by hacker_id,challenge_id
-- order by hacker_id) tab where tab.max_score <> 0)tab2
-- group by tab2.hacker_id) subs on h.hacker_id = subs.hacker_id
-- order by subs.total_score desc,h.name asc

SELECT h.hacker_id, h.name, SUM(MAX_SCORE.t1) as total_score
FROM Hackers h inner join 
(
    SELECT MAX(s.score) as t1, s.hacker_id  
    FROM Submissions s
    GROUP BY s.challenge_id, s.hacker_id
    HAVING t1 > 0
) AS MAX_SCORE
ON h.hacker_id = MAX_SCORE.hacker_id
GROUP BY h.hacker_id, h.name
ORDER BY total_score DESC, hacker_id ASC
