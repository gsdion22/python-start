import unittest


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

class TestInsertionSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(insertion_sort([]), [])

    def test_one_element_array(self):
        self.assertEqual(insertion_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(insertion_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

class TestSelectionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_one_element(self):
        self.assertEqual(selection_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(selection_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(bubble_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()