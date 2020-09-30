'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# XOR a number with itself odd number of times the result is number itself.
# XOR a number even number of times with itself, the result is 0.
# Also XOR with 0 is always the number itself.

def single_number(arr):
    # single is first in an array
    single = arr[0]
    # looping through the length of array starting with 1
    for i in range(1, len(arr)):
        # find a way to get all nums that show twice to not show at all
        # XOR all the elements since nums that shows twice that XOR with itself will be 0,
        # except the singe num that it will be the num itself
        single ^= arr[i]
    return single


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")