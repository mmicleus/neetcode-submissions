from collections import defaultdict

class Solution:
    def minWindow(self,s: str, t: str) -> str:

        s_letter_count, t_letter_count = defaultdict(int) , defaultdict(int)

        res = [-1,-1]
        resLen = float("infinity")


        if s == "":
            return ""

        for i in range(len(t)):
            t_letter_count[t[i]] += 1

        l = 0
        have = 0
        need = len(t_letter_count)

        for r in range(len(s)):

            s_letter_count[s[r]] += 1

            if (s[r] in t_letter_count) and (s_letter_count[s[r]] == t_letter_count[s[r]]):
                have += 1

            while have == need:

                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                


                s_letter_count[s[l]] -= 1

                if  (s[l] in t_letter_count) and  (s_letter_count[s[l]] < t_letter_count[s[l]]):
                    have -= 1

                l += 1


        l,r = res
        return s[l:r + 1] if (resLen != float("infinity") ) else ""
                





        



        