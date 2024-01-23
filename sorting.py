# %%
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] < array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array


def selection_sort(array):
    for i in range(len(array)):
        s = i  # smallest
        for j in range(i + 1, len(array)):
            if array[j] < array[s]:
                s = j
        array[i], array[s] = array[s], array[i]
    return array


def bubble_sort(array):
    for i in range(len(array) - 1):
        has_swapped = False
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                has_swapped = True
        if not has_swapped:
            break
    return array


# %%
ar = [17, 59, 23, 70, 11, 42, 10, 31, 95, 20]
bubble_sort(ar)
