import sys
sys.setrecursionlimit(1000001)

def fibo(n, answer):
    if n < 2: return 1
    if answer[n] == 0:      # 주어진 위치의 피보나치 수가 구해지지 않은 경우에만 재귀함수 호출
        answer[n] = fibo(n-1, answer) + fibo(n-2, answer)
    
    return answer[n]

def solution(n):
    answer = [0] * n
    answer[0] = answer[1] = 1
    
    fibo(n-1, answer)
    
    return answer[-1] % 1234567


""" 메모리를 더 줄이기 위한 방법 """
# n 번째 피보나치 수만 알면 되기 때문에 그 전의 값들을 모두 가지고 있을 필요가 없다.
# 그래서 변수 2 개로 계속해서 계산해 나가면 메모리를 덜 사용해도 된다.
# def solution(n):
#     a, b = 0, 1
    
#     for i in range(n):
#         a, b = b, a + b
    
#     return a % 1234567