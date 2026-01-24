SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO I
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID ASC

/*
1. ITEM_TREE 테이블에서, ITEM_ID와 PARENT_ITEM_ID에 각각 인덱스가 걸려 있다면, 어떤 방식이 성능상 유리할까요?
    ROOT 아이템은 대게 전체 데이터 중 극소수입니다. 
    따라서 ITEM_TREE 테이블에서 PARENT_ITEM_ID IS NULL 인 행을 인덱스로 빠르게 찾아낸 뒤, 
    해당 ITEM_ID만 ITEM_INFO 테이블에서 조회하는 방식이 효율적입니다.
    SQL 옵티마이저가 대게 이 경로를 선택하지만, 데이터 양이 수백만 건이라면 조인 순서를 제어하는 힌트를 고민해 볼 수 있습니다.
*/