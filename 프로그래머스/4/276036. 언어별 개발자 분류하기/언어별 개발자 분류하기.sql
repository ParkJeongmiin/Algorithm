WITH SKILL_MASKS AS (
    SELECT
        (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') AS FRONT_END_MASK, 
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') AS PYTHON_MASK, 
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') AS CSHARP_MASK
)
SELECT *
FROM (
    SELECT
        CASE
            WHEN (SKILL_CODE & FRONT_END_MASK) > 0 AND (SKILL_CODE & PYTHON_MASK) > 0 THEN 'A'
            WHEN (SKILL_CODE & CSHARP_MASK) > 0 THEN 'B'
            WHEN (SKILL_CODE & FRONT_END_MASK) > 0 THEN 'C'
        END AS GRADE, 
        ID, EMAIL
    FROM DEVELOPERS, SKILL_MASKS
) AS RESULT
WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC

/*
1. 왜 스킬 코드를 문자열이 아닌 2의 제곱수(Bit)로 저장했을까요?
    한 컬럼에 여러 스킬을 저장하면서 검색 속도를 극대화 할 수 있기 때문입니다.
    문자열 검색(LIKE)이 베해 비트 연산은 CPU 수준에서 가장 빠르게 처리되는 연산입니다.
    또한, 저장 공간을 매우 적게 차지합니다.
    
2. 만약 FRONT END 스킬이 100개로 늘어난다면 위 쿼리의 성능은 어떻게 될까요?
    FRONT 스킬이 아무리 늘어나도 SUM을 통해 하나의 마스크로 합쳐두면, 
    개별 개발자를 검사하는 연산 횟수는 동일합니다. 따라서 매우 뛰어난 확장성을 보입니다.
    
3. SUM(CODE)를 구할 때 주의할 점이 있다면 무엇일까요?
    데이터 타입의 한계(Overflow)를 조심해야 합니다.
    비트가 아주 많아져서 CODE의 합이 정수형의 범위를 넘어설 경우 오버플로우가 발생할 수 있습니다.
    이럴 때는 BIGINT 타입을 사용하거나 비트 연산 전용 함수를 사용해야 합니다.
*/
