def shake_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        # Resetează flag-ul de interschimbare la fiecare început al buclei
        swapped = False

        # Merge înainte și interschimbă elementele dacă ele sunt în ordine greșită
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Dacă nu s-au făcut interschimbări, lista este sortată
        if (swapped == False):
            break

        # Actualizează limita superioară, deoarece ultimul element este deja la locul lui
        end = end-1

        # Resetează flag-ul de interschimbare
        swapped = False

        # Merge înapoi și interschimbă elementele dacă ele sunt în ordine greșită
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Actualizează limita inferioară, deoarece primul element este deja la locul lui
        start = start + 1

# Exemplu de utilizare
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
shake_sort(my_list)
print("Lista sortată:", my_list)

def example_kw_only(arg, *, kw_only1, kw_only2):
    # Corpul funcției
    pass



def func(**args):
    pass

func(num = 3)

def sort(*, key=None,reverse=None):
    pass

pivot = 4
[x for x in list if x < pivot]