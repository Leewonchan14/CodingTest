-- 코드를 입력하세요
SELECT
    SUBSTR(PRODUCT_CODE,1,2) as CATEGORY,
    count(*) as PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY