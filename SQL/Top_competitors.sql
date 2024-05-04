/*
Julia conducted a  days of learning SQL contest. The start date of the contest was March 01, 2016 and the end date was March 15, 2016.

Write a query to print total number of unique hackers who made at least  submission each day (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.
*/

select h.hacker_id,h.name
from Hackers h join Submissions S on h.hacker_id = s.hacker_id
                        join Challenges C on s.challenge_id=c.challenge_id
                        join Difficulty d on c.difficulty_level=d.difficulty_level
where s.score=d.score and c.difficulty_level=d.difficulty_level
GROUP BY H.HACKER_ID, H.NAME
HAVING COUNT(S.HACKER_ID) > 1
ORDER BY COUNT(S.HACKER_ID) DESC, S.HACKER_ID ASC;
