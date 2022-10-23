# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:02:36 2022

@author: abhis
"""
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False

        
        
        pair = [['(', ')'], ['[', ']'], ['{', '}']]
        stack = []

        for i in s:
            for j in pair:
                if i in j[0]:
                    stack.append(i)
                elif i in j[1]:
                    if len(stack)==0 or stack[-1] != j[0]:
                        return False
                    else:
                        stack.pop(-1)
        if len(stack)==0:
            return True
        else:
            return False