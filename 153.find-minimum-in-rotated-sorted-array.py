# @lcpr-before-debug-begin
from python3problem153 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=153 lang=python3
# @lcpr version=30109
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
        return res

# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
