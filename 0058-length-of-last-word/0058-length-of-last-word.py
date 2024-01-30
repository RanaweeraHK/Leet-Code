class Solution(object):
    def lengthOfLastWord(self, s):
        list1 = s.strip().split()
        
        if not list1:
            return 0
        last_word = list1[-1]
        return (len(last_word))
        