class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        n=len(heights)
        i=0
        j=n-1
        while i<j:
            width=j-i
            h=min(heights[i], heights[j])
            area=width*h
            maxwater=max(area, maxwater)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxwater