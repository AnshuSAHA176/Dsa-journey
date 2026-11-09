class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water=0
        lp=0
        rp=len(height)-1
        while (lp<rp):
           
            max_water=max(max_water,min(height[lp],height[rp])*(rp-lp))
            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        return max_water