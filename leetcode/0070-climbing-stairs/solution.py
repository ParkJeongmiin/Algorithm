class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev_2_stairs = 1  # (n-2) 번 째 계단까지 경우의 수
        prev_1_stairs = 2  # (n-1) 번 째 계단까지 경우의 수

        for _ in range(3, n + 1):
            current = prev_1_stairs + prev_2_stairs

            prev_2_stairs = prev_1_stairs  # (n-2) -> (n-1)
            prev_1_stairs = current  # (n-1) -> current value

        return prev_1_stairs

