# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 05:22:50 2022

@author: abhis

"""

##3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
    
        mx_len =0
        
        result = []
        
        index = 0
        
        while index < len(s):
            longest = ''
            
            for i in range(index, len(s)):
                
                if s[i] in longest: break
                else:
                    longest = longest + s[i] 
                    
                
            len(longest) > mx_len
            mx_len = len(longest)
                        
                        
            result.append(mx_len)
                        
            index = index + 1
            
        return max(result)