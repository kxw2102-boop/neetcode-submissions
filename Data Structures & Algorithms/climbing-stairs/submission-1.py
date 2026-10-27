class Solution:
    def climbStairs(self, n: int) -> int:
        #cache={4:5} means calculated f(4)=5 and kept
        #cache[4] = 5 means taking the kept value
        #recursion + cache = memoization
        #if n == 1:
            #return 1

        #if n == 2:
            #return 2

        #return self.climbStairs(n-1) + self.climbStairs(n-2)
        #time limit exceeded

        cache = {}
        def ways(k):
            if k <= 2:
                return k

            if k in cache:
                return cache[k]

            cache[k] = ways(k-1) + ways(k-2)
            return cache[k]

            
        return ways(n)



        