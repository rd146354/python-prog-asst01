# Python program for implementation of Bubble Sort
# Acknowledgement: GeeksforGeeks


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        q = len(arr) - 1
        while q >= 0:
            print(arr[q])
            q -= 1


# Driver code to test above
arr = ['word', 'syllable', 'pentameter', 'punctuation', 'pause', 'lexicon', 'iconography']

bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%s" % arr[i])
