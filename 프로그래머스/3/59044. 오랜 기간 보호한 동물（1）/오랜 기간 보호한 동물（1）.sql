-- 코드를 입력하세요
SELECT AI.NAME, AI.DATETIME 
FROM ANIMAL_INS AI
WHERE AI.ANIMAL_ID NOT IN (
    SELECT AO.ANIMAL_ID
    FROM ANIMAL_OUTS AO
)
ORDER BY AI.DATETIME ASC
LIMIT 3