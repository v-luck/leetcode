class Solution(object):
    def reverse(self, x):
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        reverse = int(str(x)[::-1])
        if is_negative:
            reverse *= -1
        if (abs(reverse) > (2 ** 31 -1)):
            return 0
        return (reverse)

dog = Solution()
print(dog.reverse(1534236469))