import unittest
from Manager.sortari import selection_sort, shake_sort


class TestSortingManager(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual(selection_sort([[34, 5], [5, 2], [4, 34]], key=lambda x: x[1], cmp=lambda x, y: x > y),
                         [[5, 2], [34, 5], [4, 34]])
        self.assertEqual(selection_sort([]), [])

    def test_shake_sort(self):
        l = [[43, 44], [55, 66], [77, 88], [2334, 45],[5, 65], [6, 3]]
        l_sorted = [[77, 88], [55, 66], [5, 65], [2334, 45], [43, 44], [6, 3]]
        self.assertEqual(shake_sort(l, key=lambda x: x[1], reverse=True), l_sorted)
        self.assertEqual(shake_sort([]), [])
