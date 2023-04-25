from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_lens = [len(s) for s in strs]
        min_idx = s_lens.index(min(s_lens))
        terminate = False
        prefix = ""
        for i in range(len(strs[min_idx])):
            ch = strs[min_idx][i]
            for j in range(len(strs)):
                if strs[j][i] != ch:
                    terminate = True
                    break

            if terminate:
                break
            else:
                prefix += ch

        return prefix
    

class SolutionFaster:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        srtd_strs = sorted(strs)
        first = srtd_strs[0]
        last = srtd_strs[-1]
        res = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res