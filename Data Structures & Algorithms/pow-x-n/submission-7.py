class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Track if the original power was negative
        is_negative = n < 0
        n = abs(n)

        ans = 1.0

        # 2. Binary Exponentiation Loop
        while n > 0:
            if (n & 1) == 1:
                ans *= x
            x *= x      
            n >>= 1     
            
        # 3. Return the reciprocal if n was originally negative
        return 1.0 / ans if is_negative else ans

