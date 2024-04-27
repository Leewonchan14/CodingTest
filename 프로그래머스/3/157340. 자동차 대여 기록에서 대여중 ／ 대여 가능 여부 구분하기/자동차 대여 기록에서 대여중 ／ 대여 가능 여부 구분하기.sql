-- 코드를 입력하세요
SELECT DISTINCT C1.CAR_ID, 
    CASE 
        WHEN 
            C1.CAR_ID IN (
                SELECT DISTINCT C2.CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C2
                WHERE DATE_FORMAT(C2.START_DATE, "%Y-%m-%d") <= "2022-10-16" 
                AND DATE_FORMAT(C2.END_DATE, "%Y-%m-%d") >= "2022-10-16"
            ) THEN "대여중"
        ELSE "대여 가능"
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C1
ORDER BY C1.CAR_ID DESC