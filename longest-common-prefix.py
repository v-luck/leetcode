class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        longest_prefix = ""
        shortest_word = strs[0]
        # removes errors for wrong indexing
        for word in strs:
            if len(word) < len(shortest_word):
                shortest_word = word
        for index, letter in enumerate(shortest_word):
            if all(word[index] == letter for word in strs):
                longest_prefix += letter
            else:
                break
        return longest_prefix

flowers = ["", "b"]
dog = Solution()
print(dog.longestCommonPrefix(flowers))





