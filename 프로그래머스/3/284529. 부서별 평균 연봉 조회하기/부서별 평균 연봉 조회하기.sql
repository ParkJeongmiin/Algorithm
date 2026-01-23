SELECT A.DEPT_ID, D.DEPT_NAME_EN, A.AVG_SAL
FROM (
    SELECT DEPT_ID, ROUND(AVG(SAL), 0) AS AVG_SAL
    FROM HR_EMPLOYEES
    GROUP BY DEPT_ID
) AS A
JOIN HR_DEPARTMENT D ON A.DEPT_ID = D.DEPT_ID
ORDER BY AVG_SAL DESC

/*
1. 만약 사원이 한 명도 없는 부서가 있다면, 위의 쿼리 결과에 그 부서가 나올까요?
    서브 쿼리에서 집계 시와 INNER JOIN을 수행했기 때문에 사원이 없는 부서는 출력되지 않습니다.
    만약 모든 부서를 다 보여줘야 한다면 HR_DEPARTMENT 테이블 기준으로 LEFT JOIN을 수행해야 합니다.

2. FOUND(AVG(SAL), 0) 연산 시, SAL이 INT가 아닐 경우 발생할 수 있는 '부동 소수점 오차'에 대해서 알고 있나요?
    정밀한 금융 데이터를 다룰 때는 FLOAT 대신 DECIMAL 타입을 사용해 오차를 방지해야 합니다.
    연봉 데이터는 일반적으로 정수 범위 내에서 처리되므로 큰 무리는 없습니다.
    
3. 수천만 건의 사원 데이터가 있을 때, 이 쿼리를 위해 어떤 인덱스를 생성하시겠습니까?
    (DEPT_ID, SAL) 복합 인덱스를 제안합니다.
    DEPT_NO로 그룹화를 진행하고, SAL로 즉시 읽어 평균을 낼 수 있습니다.
*/