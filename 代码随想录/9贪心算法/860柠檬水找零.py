from typing import *


class Solution:
    """
    因为找零只有3种情况，所以直接if else即可。贪心体现在找零15的时候，我们优先用10+5的组合，因为我们要尽可能的保留更多的5！
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change = bill - 5
            money[bill] += 1
            if change == 0:  # 不用找零
                continue
            elif change == 5:
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            else:  # change == 15，优先找零10+5因为5才是我们想要保留的（方便之后的找零），其次3*5
                if money[10] > 0 and money[5] > 0:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
        return True








