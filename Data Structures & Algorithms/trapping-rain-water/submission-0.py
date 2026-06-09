class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        n=len(height)

        for i in range(n):

            left_max=0
            for j in range(i+1):
                left_max=max(left_max, height[j])
            right_max=0
            for k in range(i, n):
                right_max=max(right_max, height[k])
            
            water+=min(left_max, right_max)-height[i]
        return water
