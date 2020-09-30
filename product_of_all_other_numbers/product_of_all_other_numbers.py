'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # loop through the array
    # multiple everything in that array but the specific value in the index
        # In order to multiple everything but that self value,
        # need to split the array in halves with a LHS & RHS
        # only multiple values in the left of that index value 
        # only multiple values in the right of that index value
    # return the product and that is added onto an arr
    # the product is the value in the index not multipled in the new arr
   
    # creating a placeholder for each 3 arrays with 0s
    L = [0]*len(arr)
    R = [0]*len(arr)
    product = [0]*len(arr) 

    L[0] = 1 # first value in the left array is 1 since there is 
             # no values in the left to start with to multiply

    for i in range(1, len(arr)): # loop through the left array starting at 1
        L[i] = arr[i - 1] * L[i - 1] # left array index value is the value in 
                                     # the original array * the previous value 
                                     # in the L array
                                     # ex: i = 4, L[4] = arr[4-1] * L[4-1]
                                     # L[4] = arr[3] * L[3]
                                     # L[4] = 8 * 108
                                     # L[4] = 864
        
    R[len(arr) - 1] = 1 # first value at the end of the right array is 1
    # it is going back to multiple all the values on the right side of the array
    for i in reversed(range(len(arr) - 1)): # loop through the right array in reverse starting at 1
        R[i] = arr[i + 1] * R[i + 1] # just like the left array but opposite so its + 1
         
    for i in range(len(arr)): # loop through the final third array which is all products
        product[i] = L[i] * R[i] # multiple the left and right together for product in that index
        
    return product # return the array with the products
   

if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
