# TC:0(N)
# SC:O(1)
class Solution:
    def __init__(self):
        self.ones = [" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                     "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        self.tens = [" ", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = [" ", "Thousand", "Million", "Billion"]

    def numberToWords(self, num) :
        if num == 0:
            return "Zero"
        result = " "
        index = 0  #
        while num > 0:
            # divide into triplets
            if num % 1000 != 0:
                result = self.helper(num % 1000) + self.thousands[index] + " " + result
            num = num // 1000
            index += 1
        return result.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.ones[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.ones[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)


