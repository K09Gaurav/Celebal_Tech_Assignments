-- Task 1

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY LIKE '[aeiou]%' AND CITY LIKE '%[aeiou]'
;

--Task 2
SELECT (MAX(POPULATION) - MIN(POPULATION))
FROM CITY;

--Task 3
SELECT ROUND(
        SQRT(POWER(((MAX(lAT_N))-(MIN(LAT_N))),2)
             +
             POWER(((MAX(lONG_W))-(MIN(lONG_W))),2) 
        ),4)
FROM STATION

--Task 4
SELECT ROUND(MEDIAN(LAT_N),4)
FROM STATION
ORDER BY LAT_N ASC;

--Task 5
select c.name
from    city c inner join country cn
on c.countrycode = cn.code
where cn.continent = "Africa"

--TASK 6
select c.name
from    city c inner join country cn
on c.countrycode = cn.code
where cn.continent = "Africa"

--Task 7
select
    s.name,
    g.grade,
    s.marks
from
    students s
    left join
    grades g
ON s.marks >= g.Min_mark AND s.marks <= g.Max_mark
where g.grade > 7
order by g.grade desc, s.name ,s.marks;

select
    null,
    g.grade,
    s.marks
from
    students s
    left join
    grades g
ON s.marks BETWEEN g.Min_mark AND g.Max_mark
where g.grade < 8
order by g.grade desc, s.name ,s.marks;


--Task 8
select h.hacker_id, h.name
from
    Submissions s
    INNER JOIN
    Challenges ch
ON ch.challenge_id = s.challenge_id
    INNER JOIN
    difficulty d
ON ch.difficulty_level = d.difficulty_level
    INNER JOIN
    hackers h
ON h.hacker_id = s.hacker_id
where s.score = d.score AND d.difficulty_level = ch.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id)>1
order by count(s.hacker_id) desc, s.hacker_id

--Task 9
select w.id, p.age, w.coins_needed, w.power 
from Wands as w 
join 
Wands_Property as p on (w.code = p.code) 
where p.is_evil = 0 
and 
w.coins_needed = (select min(coins_needed) 
                  from Wands as w1 
                  join Wands_Property as p1 on (w1.code = p1.code) 
                  where w1.power = w.power and p1.age = p.age)
                  order by w.power desc, p.age desc

--Task 10
select h.hacker_id, h.name , sum(s.marks) as total 
from hackers h 
left join (select hacker_id,challenge_id,max(score) as marks 
           from submissions 
           group by hacker_id,challenge_id) s on h.hacker_id=s.hacker_id 
           group by h.hacker_id,h.name 
           having total > 0 
           order by total desc, h.hacker_id asc ;