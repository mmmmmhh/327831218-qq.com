# 1 两数之和
# 方法一：基本方法，嵌套for循环。
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if target == nums[i] + nums[j]:
                    return i, j
                    
# 方法二：只用一次for循环，判断target-nums[i]是否在列表中，在 则用list.index()获取索引，注意判断返回的两个数下标不能相同。
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums:
                if i != nums.index(target - nums[i]):
                    return i, nums.index(target - nums[i])
                    
# 方法三: hash table 即字典 key-value O(1)
# 遍历一个 i ，就把nums[i]放在字典里，之后 i 不断增加，遇到target-nums[i]在字典里的情况，return即可。
# 注意，先return dict[a]，后return i，因为dict里存的value是先索引到的下标，i是后索引到的下标。
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dict:
                return dict[a], i
            dict[nums[i]] = i
        
