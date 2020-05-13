# Exercise 7.3 Sorting

## Finding the smallest value

Create in the main program a function `smallest` that takes an integer array as a parameter. It should return the smallest value in the array.

Here is the structure of the method:

```python
def smallest(array):
    # write your code here
```

The next example illustrates how the method works:

```python
numbers = [6, 5, 8, 7, 11]
print("Smallest: " + str(smallest(numbers)))
```

```plaintext
Smallest: 5
```

## Index of the smallest value

Create a function called `index_of_smallest` in the class  It should return the index of the smallest number in the array that it receives as a parameter.

Here is the structure of the method:

```python
def index_of_smallest(array):
    # write your code here
```

The following code illustrates how to use the method:

```python
# indices:      0  1  2  3  4
numbers = [6, 5, 8, 7, 11]
print("Index of the smallest number: " + str(index_of_smallest(numbers)))
```

```plaintext
Index of the smallest number: 1
```

The smallest number in the array is 5, and its position in the array (i.e. index) is 1. Be sure to remember that indexing an array begins at 0.

## Index of the smallest value after a certain value

Create in the class MainProgram a class method called `index_of_smallest_from`. It works similarly to the method in the previous section, but only considers the table values from a certain index forwards. In addition to the table, it receives this start index as a parameter.

The structure of the method is the following:

```python
def index_of_smallest_from(table, start_index):
    # write your code here
```

The following code illustrates how the method words:

```python
# indices:       0  1  2  3   4
numbers = [-1, 6, 9, 8, 12]
print(index_of_smallest_from(numbers, 0))
print(index_of_smallest_from(numbers, 1))
print(index_of_smallest_from(numbers, 2))
```

```plaintext
0
1
3
```


In this example the first method call searches for the index of the smallest number, starting from index 0. Starting from index 0, the smallest number is -1 and its index is 0. The second method call searches for the index of the smallest value starting from index 1. In this case the smallest number is 6 and its index is 1. The third calls searches for the index of the smallest value starting at index 2. Then the smallest number is 8 and its index is 3.

## Swapping numbers

Create a class method `swap` in the class  It receives as its parameters an array and two indices inside it. The method swaps the numbers in these indices with each other.

The basic structure of the method is:

```python
def swap(array, index1, index2):
    # write your code here
```

The following illustrates how to use the method. To print an array we take use of the `__str__` class method of the class `Arrays`. It formats an array into an easily readable string.

```python
numbers = [3, 2, 5, 4, 8]

print(numbers)

swap(numbers, 1, 0)
print(numbers)

swap(numbers, 0, 3)
print(numbers)
```

```plaintext
[3, 2, 5, 4, 8]
[2, 3, 5, 4, 8]
[4, 3, 5, 2, 8]
```

## Sorting

We have now assembled a set of useful methods. With their help, we can implement a sorting algorithm known by the name of selection sort.

The idea of selection sort is:

- Move the smallest number in the array to index 0.
- Move the second smallest number to index 1.
- Move the third smallest number in the array to index 2.

- Etc.

In other words:

- Examine the array starting from index 0. Swap the following two numbers with each other: the number at index 0, and the smallest number in the array starting from index 0.
- Examine the array starting from index 1. Swap the following two numbers with each other: the number at index 1, and the smallest number in the array starting from index 1.
- Examine the array starting from index 2. Swap the following two numbers with each other: the number at index 2, and the smallest number in the array starting from index 2.
- Etc.

Implement a class method called `sort_numbers` based on the idea above in the class  It should include a loop that goes through the indices of the array. Certainly the method `index_of_smallest_from` and `swap` will come in handy. Additionally, print the contents of the arrya before sorting and after every iteration of the loop to ensure that the algorithm works as you expect it to.

The definition of the method looks like this:

```python
def sort_numbers(array):

```

Use at least the following example to test how the method functions:

```python
numbers = [8, 3, 7, 9, 1, 2, 4]
sort_numbers(numbers)
```

The output of the program should look like the print below.

```plaintext
[1, 2, 3, 4, 7, 8, 9]
```

Notice how the array becomes sorted little by little starting from the beginning and advancing towards the end of the array by printing each line of the swap!
