



class Solution:
    def findMissingandRepeating(self,nums):
        rep = 0
        miss = 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                rep = nums[i]
        print(rep)

        for i in range(1, max(nums) + 1):
            if not i in nums:
                print("Missing =", i)


sol = Solution()

sol.findMissingandRepeating([1,2,3,4,5,5,7])

