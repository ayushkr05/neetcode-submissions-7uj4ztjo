class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        n=len(height)
        for i in range(n):
            lmax=0
            for j in range(i+1):
                lmax=max(lmax, height[j])
            rmax=0
            for j in range(i, n):
                rmax=max(rmax, height[j])
            
            water+=min(lmax, rmax)-height[i]
        return water