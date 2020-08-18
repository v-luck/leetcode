class Solution(object):

    def __init__(self):
        self.my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        self.my_negative_dict = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }

    def romanToInt(self, s):
        total = 0
        for index, element in enumerate(s):
            multiplier = 1
            number = self.my_dict.get(element)
            if element in self.my_negative_dict:
                try:
                    if s[index + 1] in self.my_negative_dict.get(element):
                        multiplier *= -1
                except:
                    pass
            number *= multiplier
            total += number

        return total


dog = Solution()
print(dog.romanToInt("MCMXCIV"))




