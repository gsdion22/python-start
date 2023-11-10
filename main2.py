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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result
	
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
	
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
		
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

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(merge_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
		
class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(quick_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
		
class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(heap_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()