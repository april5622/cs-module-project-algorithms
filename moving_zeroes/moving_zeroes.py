'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr): # like merge sort code
    not_zeroes = 0
    #loop through array to find the value 0
    for i in range(len(arr)):
    # if value does NOT equal to 0
        if arr[i] != 0: # checking if the index value in the array is not 0
            # the non 0 value in the array will equal to the index value of the arr 
            # the NUM VALUE only moves to overwrite because it is a NON 0
            arr[not_zeroes] = arr[i] # the non 0 value will overwrite the previous value
            not_zeroes += 1 # count for non 0 will increase by 1
    # all other values are moved to the front and the non zero index is in the beginning
    # The 0 values will go to the end
    while not_zeroes < len(arr): # to make sure the len of the arr is still longer
        arr[not_zeroes] = 0 
        not_zeroes += 1
    # return the array with all 0 values in the end of the array
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")