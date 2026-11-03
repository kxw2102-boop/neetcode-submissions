class Solution:
    def countBits(self, n: int) -> List[int]:
        #def binrep(n):
            #return bin(n)[2:] #start after 0b from2index

        #"1011".count("1") 

        output = [] #set empty list
        for i in range(n + 1):
            countones = bin(i).count("1")
            output.append(countones)

        return output