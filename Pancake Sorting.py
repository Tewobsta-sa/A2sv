class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []

        flips = []
        n = len(arr)

        for i in range(n - 1, 0, -1):
            max_index = 0
            for j in range(1, i+1):
                if arr[j] > arr[max_index]:
                    max_index = j

            if max_index != i:
                arr[:max_index+1] = arr[:max_index+1][::-1]
                flips.append(max_index+1)

                arr[:i+1] = arr[:i+1][::-1]
                flips.append(i+1)

        return flips
