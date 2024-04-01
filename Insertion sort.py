def insertionSort1(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            print(' '.join(str(x) for x in arr))
            j -= 1
            arr[j+1] = key 
    print(' '.join(str(x) for x in arr))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
