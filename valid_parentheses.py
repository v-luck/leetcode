class Solution(object):

    def check_parantheses(self, list):
        left_bracket = ['(', '[', '{']
        bracket_dict = {'(' : ')', '[' : ']', '{' : '}'}

        for index, bracket in enumerate(list):
            newList = list[:]
            if index + 1 == len(newList):
                return False
            if bracket in left_bracket:
                if newList[index + 1] == bracket_dict.get(bracket):
                    newList.pop(index)
                    newList.pop(index)
                    return newList
                if newList[index + 1] not in left_bracket and newList[index + 1] != bracket_dict.get(bracket):
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
            string_list = self.check_parantheses(string_list)



#bracket ="(}(({(}()(({)](({["
#bracket2 ="([])"
bracket3 ="([]["
dog = Solution()
#print(dog.isValid(bracket))
#print(dog.isValid(bracket2))
print(dog.isValid(bracket3))
