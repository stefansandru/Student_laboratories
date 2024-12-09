import locale


def selection_sort(arr, *, key=None, reverse=False, cmp=None):
    """
    Sorts the elements of the list using the selection sort algorithm.

    :param arr: The list to be sorted
    :param key: Key function
    :param reverse: If True, the list is sorted in descending order
    :param cmp: Custom comparison function.
    Should take two arguments and return a negative number if the first argument is smaller,
    zero if they are equal, and a positive number if the first argument is larger.
    """
    for i in range(len(arr) - 1):
        ind = i
        for j in range(i + 1, len(arr)):
            element_i = key(arr[ind]) if key else arr[ind]
            element_j = key(arr[j]) if key else arr[j]
            try:
                comparison_result = cmp(element_i, element_j) if cmp else element_i - element_j
            except TypeError:
                comparison_result = cmp(element_i, element_j) if cmp else locale.strcoll(element_i, element_j)

            if (comparison_result > 0) if not reverse else (comparison_result < 0):
                ind = j

        if i < ind:
            arr[i], arr[ind] = arr[ind], arr[i]
    return arr


def shake_sort(arr, *, key=None, reverse=False, cmp=None):
    """
    Sorts the elements of the list using the shake sort algorithm.

    :param arr: The list to be sorted.
    :param key: Key function
    :param reverse: If True, the list is sorted in descending order.
    :param cmp: Custom comparison function.
    Should take two arguments and return a negative number if the first argument is smaller,
    zero if they are equal, and a positive number if the first argument is larger.
    """
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        for i in range(n - 1):
            element_i = key(arr[i]) if key else arr[i]
            element_next = key(arr[i + 1]) if key else arr[i + 1]
            try:
                comparison_result = cmp(element_i, element_next) if cmp else element_i - element_next
            except TypeError:
                comparison_result = cmp(element_i, element_next) if cmp else locale.strcoll(element_i, element_next)

            if (comparison_result > 0) if not reverse else (comparison_result < 0):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        for i in range(n - 2, 0, -1):
            element_i = key(arr[i]) if key else arr[i]
            element_prev = key(arr[i - 1]) if key else arr[i - 1]
            try:
                comparison_result = cmp(element_i, element_prev) if cmp else element_i - element_prev
            except TypeError:
                comparison_result = cmp(element_i, element_prev) if cmp else locale.strcoll(element_i, element_prev)

            if (comparison_result < 0) if not reverse else (comparison_result > 0):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
    return arr