class Solution(object):
    def twoSum(self, arr, target):
        index1 = 0
        index2 = len(arr) - 1

        while index1 < index2:
            current_state = arr[index1] + arr[index2]

            if current_state == target:
                return [index1+1, index2+1]
            elif current_state < target:
                index1 += 1
            else:
                index2 -= 1
                
        return []