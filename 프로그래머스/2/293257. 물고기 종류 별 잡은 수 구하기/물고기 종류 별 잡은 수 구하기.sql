SELECT T.FISH_COUNT, N.FISH_NAME
FROM (
    SELECT FISH_TYPE, COUNT(*) AS FISH_COUNT
    FROM FISH_INFO
    GROUP BY FISH_TYPE
) AS T
LEFT JOIN FISH_NAME_INFO N ON T.FISH_TYPE = N.FISH_TYPE
ORDER BY T.FISH_COUNT DESC

/*
1. FISH_INFO에 수억 건의 데이터가 있고, FISH_NAME_INFO는 수십 개라면 어떤 조인 방식이 유리할까요?
    위의 쿼리처럼 '서브 쿼리로 먼저 그룹화'를 진행해 조인 대상 집합을 최소화 하는 것이 유리합니다.
    인덱스가 FISH_TYPE에 잘 걸려있다면, 수억 건을 조인하는 비용보다 
    수십 개의 그룹으로 만든 뒤 조인하는 것이 조인하는 것이 메모리 효율 측면에서 훨씬 뛰어납니다.
    
2. 문제 설명에 '길이가 10cm' 이하일 경우 LENGTH가 NULL 이라는 조건이 있습니다.
    만약 '평균 길이'를 구해야 한다면 어떻게 처리하시겠습니까?
    
    단순히 AVG(LENGTH)를 하면 NULL 값이 제외되기 때문에 평균이 왜곡됩니다.
    문제에서 10cm이하가 NULL이라고 했으므로, COALESCE(LENGTH, 10) 또는 IFNULL(LENGTH, 10)을 사용해
    최솟값인 10으로 치환하거나, 비지니스 요건에 맞춰 적절한 보정치를 넣어햐 줭학한 통계가 나옵니다.
    
3. FISH_NAME_INFO에 없는 FISH_TYPE이 FISH_INFO에 존재한다면 어떻게 될까요?
    위 쿼리와 같은 INNER JOIN에서는 이름 정보가 없는 데이터를 결과에서 삭제합니다.
    만약 이름이 없더라도 잡은 기록을 모두 보여줘야 한다면 LEFT JOIN을 사용해 누락을 방지해야 합니다.
*/