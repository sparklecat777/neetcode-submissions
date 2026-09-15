class Solution:

    def encode(self, strs: List[str]) -> str:
        Return = ""
        for i in strs:
            Return += str(len(i)) + "#" + i
        return Return

    def decode(self, s: str) -> List[str]:
        Decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            Length = int(s[i:j])
            Decode.append(s[j+1:j+1+Length])
            i= j+1+Length
        return Decode

