# class Solution(object):
#     def twoSum(self, nums, target):
#         self.nums = nums
#         self.target = target
#     def answer(self):
#         answer=[]
#         for i in range(len(nums)):
#             for j in nums:
#                 if target-nums[i] == j:
#                     answer.append(j)
#                     break;
#                 answer.append(i)
#                 break;
#             return answer;
#             break;

# output = Solution([2,4,5,7],9)

# print(output.total)

#위와 같이 작성하면 'solution'이 인자를 받지 않는다고 나옴.

class Solution(object):
    def twoSum(self, nums, target):
        answer=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer

output = Solution()
result = output.twoSum([2,4,5,8],9)
print(result)