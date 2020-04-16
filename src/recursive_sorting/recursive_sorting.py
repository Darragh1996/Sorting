# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print("A: ", arrA, "B: ", arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    j = k = 0
    for i in range(0, len(merged_arr)):
        if j < len(arrA) and (k >= len(arrB) or arrA[j] < arrB[k]):
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1

    print("merged: ", merged_arr)
    return merged_arr


# print(merge([3], [2, 2, 7]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # print("merge sort", arr)
    if len(arr) > 1:
        split = len(arr) // 2
        left = arr[0:split]
        right = arr[split:]
        arr = merge(merge_sort(left), merge_sort(right))

    return arr


merge_sort([7, 6, 5, 8, 12, 3])


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
