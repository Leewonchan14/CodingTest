-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING 9 <= HOUR AND HOUR <= 19
ORDER BY HOUR