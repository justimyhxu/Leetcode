'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0') # 注意要去掉头部的'0'
        return ans or '0'  # 注意这里可能返回 '0'
    
    def compare(self, a, b):
        return [1,-1] [a + b > b + a] 
        # 这里是比较'12' + '21' > '21' + '12'，如果a+b > b+a, 返回-1，a< b, a放在b前面，否则返回-1
     
