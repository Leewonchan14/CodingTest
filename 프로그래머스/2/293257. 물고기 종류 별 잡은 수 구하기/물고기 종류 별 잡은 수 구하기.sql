-- 코드를 작성해주세요
SELECT count(*) AS FISH_COUNT, FI.FISH_NAME
FROM FISH_INFO F JOIN FISH_NAME_INFO FI
ON F.FISH_TYPE = FI.FISH_TYPE
GROUP BY FI.FISH_NAME
ORDER BY FISH_COUNT DESC