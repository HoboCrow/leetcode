# https://leetcode.com/problems/circular-array-loop/

from typing import List

import unittest


class Solution:
    @staticmethod
    def getDir(n):
        return 1 if n < 0 else 0

    def circularArrayLoop(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        cicle = False
        while j < len(nums):
            dir_i = self.getDir(nums[i])
            while True:
                next_i = (i + nums[i]) % len(nums)
                nums[i] = 0
                next_dir = self.getDir(nums[next_i])
                if dir_i != next_dir or next_i == i:
                    nums[next_i] = 0
                    i = j
                    j = j + 1
                    break
                if nums[next_i] == 0:
                    return True
                i = next_i
        return False
