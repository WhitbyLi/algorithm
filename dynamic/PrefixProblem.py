from typing import List


def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    n = len(nums)
    preSum = 0
    preSumIndex = {}
    preSumIndex[0] = -1
    ans = 0
    for i in range(n):
        preSum += nums[i]
        if not preSumIndex.__contains__(preSum):
            preSumIndex[preSum] = i
        if preSumIndex.__contains__(preSum - k):
            ans = max(ans, i - preSumIndex[preSum - k])
    return ans


# Jump game
def canJump(self, nums: List[int]) -> bool:
    far = 0
    n = len(nums)
    for i in range(n):
        if far < i:
            return False
        far = max(far, i + nums[i])
    return True


# Jump game II
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step


# Is Subsequence
def isSubsequence(self, s: str, t: str) -> bool:
    n, m = len(s), len(t)
    i = j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == n


# Best Time to Buy and Sell Stock II
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    for price in prices:
        if price > buy:
            profit += price - buy
        buy = price
    return profit


# Array Partition I
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    i = 0
    sum = 0
    while i < len(nums):
        sum += nums[i]
        i = i + 2
    return sum
