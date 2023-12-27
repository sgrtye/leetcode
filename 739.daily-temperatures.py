# @lcpr-before-debug-begin
from python3problem739 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=739 lang=python3
# @lcpr version=30106
#
# [739] Daily Temperatures
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)

        return result


# @lc code=end


#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#
