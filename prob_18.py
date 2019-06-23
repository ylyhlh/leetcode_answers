# 18. 4Sum
# https://leetcode.com/problems/4sum/



# solution 1: 49%
class Solution_0(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            target_for_3sum = target - nums[i]
            res_3sum = self.threeSum_withtarget(nums[i+1:], target_for_3sum)
            for res in res_3sum:
                results.append([nums[i]] + res)
        return results

    def threeSum_withtarget(self, nums, target):
        res = []
        N = len(nums)
        if N < 3: return res
        # nums.sort() # already sorted

        
        for i in range(N-2): # j k for last
            new_target = target - nums[i]
            l, r = i+1, N-1
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > new_target:
                    r -= 1 #move r
                elif cur_sum < new_target:
                    l += 1# move l
                else: # equal to target
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
        return res

# solution 2: 100% pass the results into function, 
# inmportant: stop when target is not possible 
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            if target < nums[i]*4 or target > nums[-1]*4:  # IMP: take advantages of sorted list
                break
            target_for_3sum = target - nums[i]
            self.threeSum_withtarget(nums[i+1:], target_for_3sum, nums[i], results)
            # for res in res_3sum:
            #     results.append([nums[i]] + res)
        return results

    def threeSum_withtarget(self, nums, target, comb, res):
        # res = []
        N = len(nums)
        if N < 3: return
        # nums.sort() # already sorted

        
        for i in range(N-2): # j k for last
            
            new_target = target - nums[i]
            l, r = i+1, N-1
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            if target < nums[i]*3 or target > nums[-1]*3:  # IMP: take advantages of sorted list
                break
            while l<r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > new_target:
                    r -= 1 #move r
                elif cur_sum < new_target:
                    l += 1# move l
                else: # equal to target
                    res.append([comb, nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
        return

# solution 3: very clean code from web
class Solution_2(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return