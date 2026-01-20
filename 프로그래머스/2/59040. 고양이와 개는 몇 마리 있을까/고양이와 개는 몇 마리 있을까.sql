SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY                                    # Custom sorting 추가
    CASE WHEN ANIMAL_TYPE = 'Cat' THEN 1
         WHEN ANIMAL_TYPE = 'Dog' THEN 2
    ELSE 3 END

/*
동물 종류가 100가지 인데 특정 순서로 출력해야 한다면 어떻게 해야할까?
  단순 알파벳 정렬이 아닌 커스텀 정렬을 구현해야 합니다.
  CASE WHEN이나 FILED() 함수를 사용해 정렬 우선순위를 지정할 수 있습니다.

WHERE 필터링과 HAVING 필터링의 차이는 무엇인가?
  FILTER-BEFORE-GROUP과 FILTER-AFTER-GROUP의 성능 최적화 개념
  WHERE은 그룹화 전에 필터링해 연산 대상을 줄이므로 성능상 유리하고,
  HAVING은 그룹화된 결과에 대한 조건을 걸 때 사용합니다.
*/