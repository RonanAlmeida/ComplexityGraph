"""
this module contains all the quadratic sorting functions, each of which
returns the total count of all the passes made through the inner and outer loops .
These sorting functions  are further used for generating test files and plotting their averages.

Author: Ronan Almeida
Student Number: 20178025
Date: 2019-15-11
"""


def bubble_sort(items):
    """
    bubble sort basically goes through the list, compares two items and swaps
    them if it is in incorrect order, elements bubble up to the right order. The
    count is added in both the inner/out while loop to sum the number of passes

    Parameters:
         items - a list of elements of comparable types.

    Returns:
        count - an integer sum of all the passes made through both outer/inner loops
    """

    count = 0  # setting the count to 0

    switch = True  # Switch is initially set to true, further on it is used to tells us if the list is sorted or not
    while switch:
        # this starts a new iteration at the start of the list
        # switch begins as false and turns true if and only if a swap is made

        count += 1  # increment count of outer loop

        switch = False  # set switch to false in case if list is sorted

        # starting at 1, so that a comparison can be made with the previous element i-1
        for i in range(1, len(items)):
            count += 1
            if items[i] < items[i - 1]:  # if the current element is less than the previous element
                items[i], items[i - 1] = items[i - 1], items[i]  # swap
                switch = True  # switch is true which means the list still needs to go through the loop again

    return count  # return the summed count


def insertion_sort(items):
    """
    Insertion sort essentially compares elements between one another and inserts an
    unsorted element within the right sorted index.
    The count is added in both the inner/out loops to sum the number of passes

    Parameters:
        items - a list of elements of comparable types.

    Returns:
        count - an integer sum of all the passes made through both outer and inner loops
    """
    count = 0  # count set to 0
    for i in range(1, len(items)):  # for i starting at index 1,

        count += 1  # increment outer loop

        # use j to "walk" the list from position i towards position 0
        j = i

        # while j is greater than 0 and the element on the left is
        # larger than the rightmost element
        while (j > 0) and (items[j - 1] > items[j]):
            count += 1

            # if the element on the left is larger, swap the items
            items[j - 1], items[j] = items[j], items[j - 1]
            j = j - 1  # decrease j by 1, so j can be compared with the rest of the list

    return count


def opt_bubble_sort(items):
    """
     Optimized Bubble sort Puts the elements of list items into ascending order by value.
     The only difference from bubble sort being, it cuts the length of the list by 1 every swap
     making it more efficient than bubble sort because each time it iterates through, theres a
     smaller list. The count is added in both the inner/out loops to sum the number of passes

    Parameters:
        items -  a list of elements of comparable types.

    Returns:
        count - an integer sum of all the passes made through both outer/inner loops
    """
    count = 0  # count set to 0

    n = len(items)  # n set to the length of the list, will be decreasing further as items get sorted
    swapped = True
    while swapped:
        count += 1
        swapped = False  # set swapped for false in case if list is sorted
        for i in range(1, n):  # starting at 1, so that a comparison can be made with the previous element i-1
            count += 1
            if items[i - 1] > items[i]:  # if the previous element is greater than the current element
                items[i - 1], items[i] = items[i], items[i - 1]  # swap
                swapped = True  # swapped is true which means the  still needs to go through the loop again

        n -= 1  # decrease the length of n (length of list) by 1 so that lesser comparisons can be made

    return count


def selection_sort(items):
    """
    This function implements the selection sort algorithm.  Selection sort repeatedly
    selects the smallest element in the list and puts it into the correct position.
    in the list. It does this by finding the current minimum value in the unsorted part of the list
     and placing it into the sorted part. The count is added in both the inner/out loops to sum the number of passes


    Parameters:
        items -  a list of elements of comparable types.

    Returns:
        count - an integer sum of all the passes made through both outer/inner loops
    """
    count = 0
    for i in range(len(items)):  # i going through every index in items
        count += 1

        min = i  # set minimum value to be the first value in the list, increments onward

        j = min + 1  # j is the pointer which will find the min values i+1

        # find the index of the minimum value in the list from i+1 to end
        while j < len(items):
            count += 1

            if items[j] < items[min]:  # if there exists a value less than the current min
                min = j  # set min's index to the current j's index
            j = j + 1  # increment j

        # swap the values
        items[min], items[i] = items[i], items[min]  # swap the min value with the unsorted value

    return count


if __name__ == '__main__':
    # Unit testing module to see if the total passes are being counted

    print("Uniting Testng for counting_quad_sorts Module ")

    ran_list = [6,1] # List of two elements, getting the total passes for each sort
    print("\nran_list of Two  elements: " + str(ran_list))
    print("Counting total passes for: Bubble sort: " + str(bubble_sort(ran_list)))
    print("Counting total passes for: Insertion sort: " + str(insertion_sort(ran_list)))
    print("Counting total passes for: Optimized Bubble sort: " + str(opt_bubble_sort(ran_list)))
    print("Counting total passes for: Selection sort: " + str(selection_sort(ran_list)))

    # Doubling ran_list
    ran_list = [6, 1, 5, 4] # list of four elements getting total passes for each sort
    print("\nDoubled ran_list to  Four  elements: " + str(ran_list))
    print("Counting total passes for: Bubble sort: " + str(bubble_sort(ran_list)))
    print("Counting total passes for: Insertion sort: " + str(insertion_sort(ran_list)))
    print("Counting total passes for: Optimized Bubble sort: " + str(opt_bubble_sort(ran_list)))
    print("Counting total passes for: Selection sort: " + str(selection_sort(ran_list)))
