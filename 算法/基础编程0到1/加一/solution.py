class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in range(len(digits)):
            num += digits[n] * 10 ** (len(digits) - n - 1)
        return [int(x) for x in str(num + 1)]
