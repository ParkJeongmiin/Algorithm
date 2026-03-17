SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%'
AND (O.SEX_UPON_OUTCOME LIKE 'Spayed%' OR O.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY I.ANIMAL_ID ASC

/*
1. 입양 후 중성화 여부 판단을 O.SEX_UPON_OUTCOME NOT LIKE 'Intact%' 로 작성해도 같은 결과가 출력될까요?
    논리적으로는 같은 의미이지만, '데이터 무결성'에 따라 문제가 발생할 수 있습니다.
    수정된 쿼리의 경우, Unkonwn과 같은 다른 값까지 포함되기 때문에 다른 값이 포함된 데이터가 출력될 수 있습니다.

2. 성능 최적화 관점에서 조인 순서는 중요한가요?
    현대 옵티마이저는 자동으로 최적화를 진행하지만, 원칙적으로는 데이터를 더 많이 걸러낼 수 있는 테이블을
    driving 테이블로 잡는 것이 좋습니다.
*/