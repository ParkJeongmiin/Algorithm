SELECT ROUTE, 
    CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE, 
    CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC

/*
1. ORDER BY TOTAL_DISTANCE DESC를 썼을 때 발생할 수 있는 잠재적 위험은 무엇입니까?
    CONCAT 함수 결과가 '6km'와 '12.6km' 가 있다고 가정해보겠습니다.
    숫자로 비교하면 12.6이 크기 때문에 먼저 출력되지만, 
    문자열로 비교하면 6이 1보다 크다고 판단해 '6km'가 먼저 출력되는 위험이 있습니다.
    따라서 정확한 수치 비교를 위해서는 포맷팅 전의 원본 데이터를 기준으로 정렬해야 합니다.

2. 만약 특정 역 사이 거리가 NULL이라면 AVG와 SUM 결과는 어떻게 되나요?
    집계 함수는 NULL 값을 무시하고 계산합니다.
    따라서, SUM, AVG는 존재하는 값들만 더하고 평균을 계산합니다.
    만약, NULL 값을 0으로 처리해야 한다면 IFNULL이나 COALESCE를 써야합니다.
*/