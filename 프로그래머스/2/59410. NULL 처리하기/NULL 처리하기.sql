SELECT 
    ANIMAL_TYPE, 
    COALESCE(NAME, 'No name') AS NAME, 
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

/*
1. ORDER BY 절에서 SELECT 에 포함되지 않은 ANIMAL_ID를 기준으로 정렬하는 것이 모든 상황에서 가능한가요?
    일반적인 SELECT 문에서는 가능합니다.
    SQL 실행 순서상 ORDER BY는 SELECT 절 이후에 수행되며, 원본 테이블의 모든 컬럼에 접근할 수 있기 때문입니다.
    다만, DISTINCT나 UNION을 사용해 데이터가 이미 물리적으로 축약된 경우에는 
    SELECT에 포함된 컬럼만 정렬해야 하는 제약이 생길 수 있습니다.
*/