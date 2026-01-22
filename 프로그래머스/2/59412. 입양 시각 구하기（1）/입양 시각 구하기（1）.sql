SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR
ORDER BY HOUR ASC

/*
1. 설계한 쿼리의 WHERE 절 대신 HAVING 절을 사용해서 결과를 필터링 할 수 있을까요? 그렇다면 성능 차이는 어떨까요?
    가능은 하지만 그룹화 진행 후 필터링을 진행하게 되면 CPU와 메모리 자원을 많이 소모하게 됩니다.

2. 만약 입양 기록이 아예 없는 시간대가 있다면, 설계한 쿼리 결과에 출력될까요?
    입양 기록이 없는 시간대의 데이터는 출력되지 않습니다.
    만약 모든 시간대에 대해서 출력하기를 원한다면 '재귀 쿼리(RECURSIVE CTE)'를 사용해 미리 뼈대를 만들어야 합니다.
    
3. COUNT(*)와 COUNT(NAME)을 썼을 때 결과가 달라질 수 있는 상황은 무엇입니까?
    COUNT(*)는 NULL 값이 있는 경우에 모두 포함해 갯수를 출력합니다.
    COUNT(NAME)은 NAME이 NULL인 경우 제외하고 결과를 출력하기 때문에, 
    데이터 무결성이나 요구사항에 맞게 선택해야 합니다.
*/