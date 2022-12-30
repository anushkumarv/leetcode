from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        es = ""
        n = len(strs)
        si = ""

        for s in strs:
            es += s
            si += "#" + str(len(s)) 

        es += si + "#" + str(n)

        return es
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # print(s)
        ns = 0
        ns_idx = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "#":
                ns = int(s[i+1:])
                ns_idx = i
                break

        temp = ""
        count = ns
        lens = list()
        idx = ns_idx - 1
        while count > 0:
            if s[idx] == "#":
                lens.append(int(temp))
                count -= 1
                temp = ""
            else:
                temp = s[idx] + temp
            idx -= 1

        # print(lens)
        res = list()
        for l in reversed(lens):
            ts = s[:l]
            s = s[l:]
            res.append(ts)

        return res


sol = Codec()
## time complexity - O(n)
## space complexity - O(n)
ls = ["Hello","World"]
print(ls == sol.decode(sol.encode(ls)))


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
ls = ["Hello","World"]
print(ls == sol.decode(sol.encode(ls)))