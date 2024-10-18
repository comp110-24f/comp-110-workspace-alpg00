"""This file tests the functions from utils.py"""

__author__ = "730758034"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

def test_only_evens_return_value() -> None:
    """only_evens should return a list that consists of only even numbers from the input list."""
    input: list[int] = [1, 2, 3, 4] # assigning a value to the input list.
    assert only_evens(input) == [2, 4] # checking to see if only_evens actually returns a list containing the even values form the input list.

def test_only_evens_input_value() -> None:
    """only_evens should not modify the original list, which is named input."""
    input: list[int] = [1, 2, 3, 4] # assigning a value to the input list.
    assert input == [1, 2, 3, 4] # checking to see that the input list is not modified in any way.

def test_only_evens_edge_case() -> None:
    """only_evens should return an empty list if the input list has no even values."""
    input: list[int] = [7, 9, 11] # assigning a value to the input list where there are no even values.
    assert only_evens(input) == [] # checking to see that since there are no even values, an empty list should be returned.

def test_sub_return_value() -> None:
    """sub should return a list that consists of values within the specified indexes."""
    inp: list[int] = [35, 37, 39, 41, 43, 45, 47] # assigning value to the input list named inp.
    start: int = 2 # assigning a value to the start index.
    end: int = 5 # adding a value to the end index. 
    assert sub(inp, start, end) == [39, 41, 43] # checking to see if the function only returns values within the start and end indexes, including the start index but not including the end index.

def test_sub_inp_value() -> None:
    """sub should not modify the original list, which is named inp."""
    inp: list[int] = [2, 3, 4, 5, 6, 7] # assigning value to the input list named inp.
    start: int = 2 # assigning a value to start index.
    end: int = 5 # assinging a value to end index.
    sub(inp, start, end) # calling the function with the assigned values.
    assert inp  == [2, 3, 4, 5, 6, 7] # checking to see that the input list is not changed in any way.

def test_sub_edge_case() -> None:
    """if the length of the input list is 0, sub should return the empty list."""
    inp: list[int] = [] # length of input list is 0.
    start: int = 2 # start index is 2
    end: int = 5 # end index is 5
    assert sub(inp, start, end) == [] # sub returns the empty list because the length of the list is 0.

def test_add_at_index_return_value() -> None:
    """add_at_index should return None."""
    input: list[int] = [3, 5, 7, 11] # add a list of odd integers starting at 3 and leading to 11 but missing 9.
    element: int = 9 # assigning the value 9 to the element we want to add in.
    idx: int = 3 # we want to add the element at index 3.
    assert add_at_index(input, element, idx) == None # checking to make sure that the function returns None even after passing all arguments.

def test_add_at_index_input_value() -> None:
    """add_at_index should modify its input list, which is named input, by adding the given element at the indicated index and moving everything else over."""
    input: list[int] = [4, 5, 6, 7, 9] # add a list of integers starting at 4 and ending at 9 but missing 8.
    element: int = 8 # assigning the value 8 to the element we want to add in.
    idx: int = 4 # we want to add the element at index 4.
    add_at_index(input, element, idx) # calling add_at_index with all the parameters.
    assert input == [4, 5, 6, 7, 8, 9] # checking to make sure that add_at_index modifies the input list to add in the correct element at the correct index.

def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    input: list[int] = [] # assigning an empty list to the input list.
    element: int = 5 # element we want to add to the list is 5.
    idx: int = 0 # we want to add the element at index 0
    with pytest.raises(IndexError): # we use pytest because exceptions are not returned values.
        add_at_index(input, idx, element) # checking to see that when all the parameters are passed to add_at_index, an indexerror occurs.
