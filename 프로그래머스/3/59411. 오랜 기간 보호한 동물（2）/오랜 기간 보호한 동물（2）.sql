-- 코드를 입력하세요
SELECT 
    ANIMAL_INS.ANIMAL_ID as ANIMAL_ID,
    ANIMAL_INS.NAME as NAME
FROM 
ANIMAL_INS JOIN ANIMAL_OUTS 
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
ORDER BY (ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME) Desc
LIMIT 2