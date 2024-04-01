class Solution:
    def select(self, arr, i):
        # Implement the selection algorithm
        # and return the i-th smallest element
        pass  # Replace this with your implementation

    def selectionSort(self, arr, n):
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
