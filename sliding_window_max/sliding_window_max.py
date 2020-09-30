'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # k = 3 value inside the window which is like an array within an array
    # when k moves right, within each step, that k will have the previous first index value gone
    # and append a new value into k from the array.
    # this will be a loop to have k moving right.
    # find the max value within th size of k
    # we will need to return the array with a max value from k each time it moved left


    for i in range(len(arr) - k + 1):
        return i 

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
