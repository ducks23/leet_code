class Solution:
    def reverse(self, x: int) -> int:
        i = str(abs(x))
        res = 0
        if x < 0:
            res = 0 - int(i[::-1])
        else:
            res = int(i[::-1])

        if res  < -2147483648 or res > 2147483648:
            return 0
        return res
