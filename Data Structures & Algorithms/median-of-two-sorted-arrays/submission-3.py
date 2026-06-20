class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = len(nums1) 

        total = len(nums1) + len(nums2)
        half = (total) // 2

        while left <= right:
            cut1 = (left+right) // 2 
            cut2 = half - cut1

            nums1Left = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            nums1Right = float("inf") if cut1 == len(nums1) else nums1[cut1]
            
            nums2Left = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            nums2Right = float("inf") if cut2 == len(nums2) else nums2[cut2]

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2 == 0:
                    leftMiddle = max(nums1Left, nums2Left)
                    rightMiddle = min(nums1Right, nums2Right)

                    return (leftMiddle+rightMiddle) / 2
                else:
                    return min(nums1Right, nums2Right) 
            elif nums1Left > nums2Right:
                right -= 1
            elif nums2Left > nums1Right:
                left += 1


