# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def dfs(cands, cur_target, hist):
            if cur_target == 0:
                ans.append(hist)
                return
            for k, v in enumerate(cands):
                if v > cur_target: #important trick!!!!!!!!!!!
                    break
                dfs(cands[k:], cur_target-v, hist+[v])
        dfs(candidates, target, [])
        return ans