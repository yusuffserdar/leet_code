class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def calc_median(merged):

            if len(merged) == 1:
                return merged[0]
            elif len(merged) == 0:
                return float(0)
            elif len(merged) % 2 != 0:
                return float(merged[int(len(merged) / 2)])
            else:
                return float(merged[int(len(merged) / 2) - 1] + merged[int(len(merged) / 2)]) / 2

        merged = []

        if 0 == len(nums1):
            return calc_median(nums2)

        elif 0 == len(nums2):
            return calc_median(nums1)

        else:
            i_1 = 0
            i_2 = 0

            while len(merged) != len(nums1) + len(nums2):

                if nums1[i_1] < nums2[i_2]:
                    merged.append(nums1[i_1])
                    i_1 = i_1 + 1
                    # del nums1[i_1]
                elif nums1[i_1] == nums2[i_2]:
                    merged.append(nums1[i_1])
                    i_1 = i_1 + 1
                    # del nums1[i_1]
                    merged.append(nums2[i_2])
                    # del nums2[i_2]
                    i_2 = i_2 + 1
                else:
                    # nums1[i_1] > nums2[i_2]
                    merged.append(nums2[i_2])
                    # del nums2[i_2]
                    i_2 = i_2 + 1

                if i_1 == len(nums1):
                    merged = merged + nums2[i_2:]
                    break
                elif i_2 == len(nums2):
                    merged = merged + nums1[i_1:]
                    break

        print(merged)

        return calc_median(merged)

