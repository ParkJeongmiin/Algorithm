SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME ASC

/*
1. 만약 한 동물이 여러 번 입소하고 여러 번 입양 간 기록이 있다면(1:N 관계), 위 쿼리에 어떤 문제가 생길까요?
    단순 JOIN을 수행하게 되면, ID가 중복된 데이터가 다수 존재할 수 있습니다.
    '최근 입소일'과 '최근 입양일'을 비교하는 서브쿼리나 윈도우 함수를 사용해 테이블을 구성하고 비교를 진행합니다.
*/