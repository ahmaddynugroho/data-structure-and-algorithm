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


def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j + gap], array[j] = array[j], array[j + gap]
                j -= gap
    return array


def heapify(array):
    parent_idx = len(array) // 2 - 1
    end_idx = len(array) - 1
    for idx in range(parent_idx, -1, -1):
        move_down(array, idx, end_idx)
    return array


def move_down(array, start_idx, end_idx):
    child_idx = start_idx * 2 + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] <= array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = start_idx * 2 - 1
        else:
            break


def heap_sort(array):
    heapify(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        move_down(array, 0, i - 1)
    return array


def merge_sort(ar):
    if len(ar) < 2:
        return ar
    first_half = merge_sort(ar[: len(ar) // 2])
    second_half = merge_sort(ar[len(ar) // 2 :])
    return merge(first_half, second_half)


def merge(first_half, second_half):
    res = []
    i = j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            res.append(first_half[i])
            i += 1
        else:
            res.append(second_half[j])
            j += 1
    while i < len(first_half):
        res.append(first_half[i])
        i += 1
    while j < len(second_half):
        res.append(second_half[j])
        j += 1
    return res


def quick_sort(ar):
    if len(ar) < 2:
        return ar
    return partition(ar, 0, len(ar) - 1)


def partition(ar, start, end):
    if start >= end:
        return
    pivot = end
    boundary = start
    for i in range(start, end):
        if ar[i] <= ar[pivot]:
            ar[boundary], ar[i] = ar[i], ar[boundary]
            boundary += 1
    ar[boundary], ar[end] = ar[end], ar[boundary]
    partition(ar, start, boundary - 1)
    partition(ar, boundary + 1, end)
    return ar


# %%
ar = [17, 59, 23, 70, 11, 42, 10, 31, 95, 20]
quick_sort(ar)
