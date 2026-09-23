class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""        

        aux = [str(len(s)) for s in strs]
        
        lengths = "€".join(aux)
        
        strings = "".join(strs)

        return lengths + "€" + strings

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        details = s.split("€")
        lengths = details[:-1]
        strings = details[-1]
        result = []
        
        index = 0
        for i in range(len(lengths)):
            result.append(strings[index:index+int(lengths[i])])
            index += int(lengths[i])



        return result
