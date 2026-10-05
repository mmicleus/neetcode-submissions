from collections import defaultdict

class Solution:
    def characterReplacement(self,s: str, k: int) -> int:

        letter_count = defaultdict(int)
        res = 0
        max_count = 0

        l = 0
        r = 0

        while l < len(s):

            isValid = True
            while r < len(s) and isValid:

                letter_count[s[r]] += 1
                max_count = max(letter_count[s[r]],max_count)

                if (k < ((r - l + 1) - max_count)):
                    isValid = False
                else:
                    res = max(r - l + 1,res)

                r += 1

            

            if letter_count[s[l]] == max_count:

                letter_count[s[l]] -= 1
                max_count = max(letter_count.values())
            else:
                letter_count[s[l]] -= 1

            l += 1


        return res

        