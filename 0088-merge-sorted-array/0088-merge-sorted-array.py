class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # # reduce nums1 to index m-1
        # nums1new = nums1[slice(m)]
        # # print(nums1)
        # # reduct nums2 to index n-1
        # nums2new = nums2[slice(n)]
        # # print(nums2)
        # # combine two arrays into 1
        # nums1new.extend(nums2new)
        # nums1new.sort()
        # self.nums1=nums1new
        # print(nums1)
        # print(len(nums1))
        # # sort the outpur array
        idx=0
        for i in nums2:
            nums1[m+idx] = i
            idx+=1
        nums1.sort()
        print(nums1)
        """
        Do not return anything, modify nums1 in-place instead.
        """
        