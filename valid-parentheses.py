class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parentheses_list = ['(', '[', '{']
        dict = {'(' : ')', '[' : ']', '{' : '}'}

        #checks if value is less than 2 brackets and either returns true or false
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False

        cap = 0
        while True:
            #if brackets are all removed it returns true
            if s == "":
                return True
            if cap >= len(s) - 1:
                return False

            for index, bracket in enumerate(s):
                #checks for indexes that could break indexing system
                if len(s) < 3:
                    if s[index + 1] == dict.get(bracket):
                        cap = 0
                        s = ""
                        return True
                    else:
                        return False
                #checks if it is a left bracket and not a right
                if bracket not in parentheses_list:
                    cap += 1
                    continue
                #checks if index to the right of left bracket correlates to dictionary
                print(index + 1)
                if s[index + 1] == dict.get(bracket):
                    #fixes error of index out of string
                    #splits the s string
                    s = s[:index] + s[index+2:]
                    cap = 0
                    break

print(len("(}(({(}()(({)](({["))
dog = Solution()
print(dog.isValid("(}(({(}()(({)](({["))






