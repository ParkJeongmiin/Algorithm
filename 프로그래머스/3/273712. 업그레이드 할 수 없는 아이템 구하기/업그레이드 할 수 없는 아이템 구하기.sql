SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
WHERE NOT EXISTS (
    SELECT 1
    FROM ITEM_TREE T
    WHERE T.PARENT_ITEM_ID = I.ITEM_ID
)
ORDER BY I.ITEM_ID DESC

/*
1. 만약 데이터에서 순환 참조 (A -> B -> A)가 발생한다면, 위의 쿼리는 리프 노드를 찾을 수 있을까요?
    현재 쿼리는 순환 참조에서도 동일하게 동작합니다.
    순환 구조에 퐇마된 아이템들은 모두 누군가의 부모 노드가 되므로 리프 노드가 될 수 없고, 결과에서 제외됩니다.
    다만, 순환 참조는 데이터 무결성을 해치므로 WITH RECURSIVE 쿼리를 통해 순환 여부를 먼저 검증하는 절차가 선행되어야 합니다.
*/