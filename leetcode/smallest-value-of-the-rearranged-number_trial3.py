class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        negative = num < 0
        digits = list(str(abs(num)))

        if negative:
            digits.sort(reverse=True)
            return -int("".join(digits))
        else:
            digits.sort()
            for i in range(len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int("".join(digits))