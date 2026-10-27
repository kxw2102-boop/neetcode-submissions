class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)

            x = max(stones)
            stones.remove(x)

            if x != y :
                stones.append(y-x)

            
        if len(stones) == 0:
            return 0

        return stones[0]
        