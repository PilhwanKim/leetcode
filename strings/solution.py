from typing import List
import math


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[::] = s[-1::-1]

    def reverse(self, x: int) -> int:
        reverse_str = str(x)[::-1]

        if reverse_str[-1] == '-':
            num_int = - int(reverse_str[:-1])
        else:
            num_int = int(reverse_str)

        if (1 << 31)-1 < num_int or (-1 << 31) > num_int:
            return 0

        return num_int
