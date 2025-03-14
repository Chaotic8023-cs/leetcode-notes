# 383
from typing import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a freq dict
        mag = {}
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        # loop through chars in ransomNote and try to use the counts from mag
        for c in ransomNote:
            if c not in mag or mag[c] == 0:
                return False
            mag[c] -= 1
        return True


if __name__ == '__main__':
    ransomNote = "a"
    magazine = "b"
    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))
