class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n>0):
            if n&1!=0: #check lsb is not 0 means 1 then count+=1
                count+=1
            n=n>>1 #right n by 1 menas 1011 here right sift :-0101
        return count