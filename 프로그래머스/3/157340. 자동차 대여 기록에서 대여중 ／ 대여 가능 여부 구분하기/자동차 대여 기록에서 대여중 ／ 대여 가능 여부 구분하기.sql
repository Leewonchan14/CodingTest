-- 코드를 입력하세요
SELECT C1.CAR_ID, 
CASE
WHEN 
    SUM(
        CASE 
            WHEN 
                DATE_FORMAT(C1.START_DATE, "%Y-%m-%d") <= "2022-10-16" 
                AND DATE_FORMAT(C1.END_DATE, "%Y-%m-%d") >= "2022-10-16"
            THEN 1
            ELSE 0
        END) >= 1 THEN "대여중"
        ELSE "대여 가능"
END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C1
GROUP BY C1.CAR_ID
ORDER BY C1.CAR_ID DESC