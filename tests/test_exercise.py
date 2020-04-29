import pytest
from src.exercise import smallest, index_of_smallest, index_of_smallest_from, swap, sort

def test_exercise():
    numbers = [6, 5, 8, 7, 11]

    assert smallest(numbers) == 5
    assert index_of_smallest(numbers) == 1
    assert index_of_smallest_from(numbers, 2) == 3

    swap(numbers, 1, 0)

    assert numbers == [5, 6, 8, 7, 11]

    sort(numbers)

    assert numbers == [5, 6, 7, 8, 11]
