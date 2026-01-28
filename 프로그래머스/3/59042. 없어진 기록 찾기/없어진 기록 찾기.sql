SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
WHERE NOT EXISTS (
    SELECT 1
    FROM ANIMAL_INS I
    WHERE I.ANIMAL_ID = O.ANIMAL_ID
)
ORDER BY O.ANIMAL_ID ASC


/*
1. 차집합을 계산할 때 위의 쿼리말고 다른 방법이 있을까요?
    OUTS 테이블을 기준으로 LEFT JOIN 수행 후, INS 테이블의 ID가 NULL인 데이터만 필터링하면 됩니다.
    하지만 데이터 규모가 커지게 되면, 두 테이블을 합친 뒤 필터링 하는 JOIN 방식보다, 존재하지 않는 즉시 스캔을 중단하는 NOT EXISTS 방식을 추천합니다.
    
2. LEFT JOIN 방식을 사용한다면 그 대신에 'NOT IN'을 사용해도 결과가 같을까요? 주의할 점은 무엇입니까?
    논리적으로는 같지만, I.ANIMAL_ID에 만약 NULL 값이 하나라도 섞여 있으면 NOT IN은 아무런 결과도 반환하지 않는 'Unknow' 상태에 빠집니다.
    반면에 LEFT JOIN - IS NULL 방식은 NULL 유무와 상관없이 동작합니다.
*/