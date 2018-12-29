#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution2:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
nums = [2,7,9,11]
target = 9
print(Solution2.twoSum("",nums,target))
