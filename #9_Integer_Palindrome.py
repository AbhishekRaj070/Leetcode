# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 05:29:00 2022

@author: abhis
"""
#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x)==1:
            return True
        elif len(x)==2 and x[0]==x[1]:
            return True
        else:
            if x[0]==x[-1] and self.isPalindrome(x[1:-1]):
                return True
            else:
                return False