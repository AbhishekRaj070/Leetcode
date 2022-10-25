# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:36:04 2022

@author: abhis
"""
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        high = len(nums)
        low = 0
        mid = (high+low)//2
        
        if target > nums[-1]:
            return len(nums)
        
        while mid > 0 :
                
            if nums[mid]> target:
                if target> nums[mid-1]:
                    return mid
                else:
                    high = mid
                
            
            elif nums[mid] ==target:
                break
                
            else:
                if target< nums[mid+1]:
                    return mid+1
                else:
                    
                    low = mid
                
                
                
            mid = (high + low)//2
            
        return mid 