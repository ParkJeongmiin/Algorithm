SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES, 
        RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RNK
    FROM REST_INFO
) AS SUB
WHERE RNK = 1
ORDER BY FOOD_TYPE DESC

/*
1. RANK(), DENSE_RANK(), ROW_NUMBER()의 차이와 문제 상황에 대입해 설명해 보세요.
    RANK()는 공동 순위가 존재하고, 공동 순위 만큼 다음 순위가 밀리게 됩니다.
    DENSE_RANK()는 공동 순위가 존재하고, 다음 순위에는 영향을 미치지 않습니다.
    ROW_NUMBER()는 순서대로 번호가 올라가는 합수 입니다.
    RANK는 가장 많은 식당들을 모두 출력할 때 사용, ROW_NUMBER는 무조건 하나만 출력할 때 사용
    
2. 만약 서브 쿼리를 쓰지 않고, WHERE (FOOD_TYPE, FAVORITES) IN ... 방식을 사용한다면 장단점은?
    윈도우 함수 사용 시에는 보통 한 번의 스캔으로 순위까지 계산 가능하기 때문에 연산 속도가 빨라지고, 
    코드가 길어질 경우 가독성이 좋습니다. 또한 출력 순위를 조절할 때 WHERE 절만 수정하면 되기 때문에
    확장성에 용이합니다.
    IN을 사용한 서브쿼리 방식은 FOOD_TYPE과 FAVORITES에 각각 인덱스가 잘 걸려있고,
    카테고리의 종류가 데이터 전체 양에 비해 아주 적다면, 옵티마이저가 인덱스만을 이용해 MAX 값을 빠르게 찾을 수 있습니다.
    하지만 그렇지 않다면 확장성, 가독성 면에서 떨어지는 면이 있습니다.

3. 해당 테이블에 FOOD_TYPE 별로 데이터가 수백만 건이 있다고 가정할 때, 윈도우 함수 연산을 최적화하기 위한 인덱스 설계는 어떻게 하시겠습니까?
    수백만 건의 데이터에서 윈도우 함수가 느려지는 이유는 대량의 데이터를 정렬(Filsesort)하기 때문입니다.
    이를 최적화하기 위해 (FOOD_TYPE, FAVORITES DESC) 복합 인덱스를 제안합니다.
    이 인덱스는 데이터를 음식 종류 별로 모으고, 즐겨찾기 수가 큰 순서대로 미리 정렬하기 때문에, 
    DB에서 별도의 연산 없이 인덱스를 읽는 것만으로 순위를 계산할 수 있습니다.
    또한, 쿼리에 필요한 모든 컬럼을 인덱스에 포함시킨다면 "커버링 인덱스"로 동작해
    실제 테이블에 접근조차 필요 없어지므로 성능이 극대화 됩니다.
    
    - PARTITION BY + ORDER BY -> 수백만 건의 데이터 모아서 줄 세우기 -> Filesort (성능 저하 주범)
    - (FOOD_TYPE, FAVORITES DESC) 복합 인덱스 = 미리 정렬해둔 별도의 리스트
        -> 인덱스를 생성하면서 이미 그룹화와 정렬이 되어 있습니다.
    - 인덱스가 없을 때는 그룹, 정렬을 수행하지만, 인덱스가 있다면 이미 그룹과 정렬이 끝난 상태
        -> 읽기만 하면 되기 때문에 속도가 빨라짐
*/