class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        n = abs(n)
        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans = ans * x
                n = n // 2
                x = x * x
            else:
                x = x * x
                n = n // 2

        return 1.0 / ans if is_negative else ans

