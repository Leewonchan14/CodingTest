-- 코드를 입력하세요
SELECT AIN.NAME, AIN.DATETIME FROM ANIMAL_INS AIN LEFT OUTER JOIN ANIMAL_OUTS AOUT ON AIN.ANIMAL_ID = AOUT.ANIMAL_ID WHERE AOUT.DATETIME IS NULL ORDER BY AIN.DATETIME LIMIT 3;