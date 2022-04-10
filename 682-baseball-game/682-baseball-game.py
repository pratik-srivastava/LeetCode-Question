from collections import deque

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = deque()

        push, pop = stk.append, stk.pop

        for e in ops:
            if e == '+':
                push(stk[-1] + stk[-2])
            elif e == 'D':
                push(2 * stk[-1])
            elif e == 'C':
                pop()
            else:
                push(int(e))

        return sum(stk)