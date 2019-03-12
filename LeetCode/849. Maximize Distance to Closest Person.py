class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, j = 0, len(seats)-1
        while not seats[i] or not seats[j]:
            if not seats[i]:
                i += 1
            if not seats[j]:
                j -= 1
        maxZero, i = max(i, len(seats)-1-j) * 2 - 1, 0
        while i < len(seats):
            zero = 0
            while i < len(seats) and not seats[i]:
                zero += 1
                i += 1
            maxZero = max(maxZero, zero)
            i += 1
        return (maxZero + 1) // 2
