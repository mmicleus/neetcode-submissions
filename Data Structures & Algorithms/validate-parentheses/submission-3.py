class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = []

        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for i in range(len(s)):
            if s[i] in {'{', '[','('}:
                brackets.append(s[i])
            elif not brackets or brackets[-1] != pairs[s[i]]:
                return False
            else: 
                brackets.pop()


        

        return True if not brackets else False
        