#给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答
#案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] =
#2+7 =9,所以返回[0,1]

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i+1:]:
                return [i, nums.index(num,i+1)]

solution = Solution()
list = [2,7,11,15]
target = 13
nums = solution.twoSum(list,target)
print(nums)

#index()方法语法：str.index(str, beg=0, end=len(string))
#str – 指定检索的字符串,beg – 开始索引，默认为0。,end – 结束索引，默认为字符串的长度。
#返回值：如果包含子字符串返回开始的索引值，否则抛出异常。