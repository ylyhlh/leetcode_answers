# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def dfs(cands, cur_target, index, hist):
            if cur_target == 0:
                ans.append(hist)
                return
            for k in range(index, len(cands)): 
                v = cands[k]
                if k > index and v == cands[k - 1]:
                    continue
                if v > cur_target: #important trick!!!!!!!!!!!
                    break
                
                dfs(cands, cur_target-v, k+1, hist+[v])
        dfs(candidates, target, 0, [])
        return ans