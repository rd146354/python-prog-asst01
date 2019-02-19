# Python program for implementation of Insertion Sort
# Acknowledgement: InteractivePython


def insertion_sort(alist):
    # Iterate through each item in the list
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        # Compares alist at position - 1 to a stored value
        while position > 0 and alist[position - 1] < current_value:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current_value
        print(alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


insertion_sort(alist)
print(alist)
