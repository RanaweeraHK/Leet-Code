class Solution(object):
    def plusOne(self, digits):
        s = [str(i) for i in digits]
        num = int("".join(s))
        num=num+1
        new = [int(ele) for ele in str(num)]
        return new