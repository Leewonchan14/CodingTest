-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID,
DATE_FORMAT(START_DATE, "%Y-%m-%d") as START_DATE,
DATE_FORMAT(END_DATE, "%Y-%m-%d") as END_DATE,
case
    when datediff(end_date, start_date) >= 29 then "장기 대여"
    else "단기 대여"
end as RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE "2022-09%"
ORDER BY HISTORY_ID DESC;