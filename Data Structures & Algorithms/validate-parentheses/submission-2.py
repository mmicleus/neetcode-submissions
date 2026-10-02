class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = []

        for i in range(len(s)):
            if s[i] in {'{', '[','('}:
                brackets.append(s[i])
            elif s[i] in {'}', ']',')'}:
                if not brackets:
                    return False
                elif s[i] == '}':
                    if brackets[-1] != '{':
                        return False
                    else: 
                        brackets.pop()
                elif s[i] == ']':
                    if brackets[-1] != '[':
                        return False
                    else: 
                        brackets.pop()
                elif s[i] == ')':
                    if brackets[-1] != '(':
                        return False
                    else: 
                        brackets.pop()

        
        return True if not brackets else False
        