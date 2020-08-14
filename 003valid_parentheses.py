class Solution(object):

    def check_parantheses(self, list):
        bracket_dict = {'(' : ')', '[' : ']', '{' : '}'}

        for index, bracket in enumerate(list):
            if index + 1 == len(list):
                return False
            if bracket in bracket_dict:
                if list[index + 1] == bracket_dict.get(bracket):
                    list.pop(index)
                    list.pop(index)
                    return True
                if list[index + 1] not in bracket_dict and list[index + 1] != bracket_dict.get(bracket):
                    return False


    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        if not s:
            return True
        string_list = []
        for character in s:
            string_list.append(character)

        while True:
            if len(string_list) == 0:
                return True
            if self.check_parantheses(string_list) == False:
                return False



#bracket ="(}(({(}()(({)](({["
#bracket2 ="([])"
bracket3 ="([]["
dog = Solution()
#print(dog.isValid(bracket))
#print(dog.isValid(bracket2))
print(dog.isValid(bracket3))
