class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        letter_counter = {}

        for ch in s:
            if ch in letter_counter:
                letter_counter[ch] += 1
            else:
                letter_counter[ch] = 1

        for ch in t:
            if ch not in letter_counter:
                return False
            else: 
                letter_counter[ch] -= 1

                if letter_counter[ch] == 0:
                    del letter_counter[ch]


        if len(letter_counter) == 0:
            return True

        return False


        