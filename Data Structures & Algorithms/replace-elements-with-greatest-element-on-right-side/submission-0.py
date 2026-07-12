class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        
        maxRight = -1
        for j in range(len(arr)-1, -1, -1):
            newMaxRight = max(maxRight, arr[j])
            arr[j] = maxRight
            maxRight = newMaxRight
        return arr