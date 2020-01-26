import random

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Driver code to test above
randomData = [random.randint(0, 100) for x in range(20)]

print ("Unsorted array is:")
for i in range(len(randomData)):
    print ("%d" %randomData[i])

insertionSort(randomData)

print ("\nSorted array is:")
for i in range(len(randomData)):
    print ("%d" %randomData[i])