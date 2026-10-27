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
        def ways(n):
            if n <= 2:
                return n

            if n in cache:
                return cache[n]

            cache[n] = ways(n-1) + ways(n-2)
            return cache[n]

            
        return ways(n)



        