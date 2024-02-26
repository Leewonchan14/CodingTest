-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
case 
WHEN NAME is null then "No name" 
else NAME 
End as NAME
, sex_upon_intake
from animal_ins order by animal_id