"""
This Module is for essentially contains one function, test_function
which writes out a test data as a csv file for a given sort.

Author: Ronan Almeida
Student Num: 20178025
Date: 2019-15-11
"""
import random  # import random for generating random floating point nums


def test_function(fn, max_n, num_tests):
    """
    This function  is for writing out test data as a csv file given the parameters,

    Parameters:
        fn -  a function passed a parameter in this case one of the sorting algorithms
        max_n -  max length of the randomly generated lists
        num_tests - the number of tests to run of each chosen list

    Returns:
        None - wirtes out test data as a csv file
    """
    # open file for writing
    out_file = open('' + fn.__name__ + '.csv', 'w')  # fn.__name is the name of the sorting algorithm

    for i in range(num_tests):  # iterate through num tests
        rand_list = [random.random() for x in range(max_n)]
        # rand_list is a randomly generated list which contains 100 random floats ranging from 0 to 0 in value

        row = []  # a list of all the count passes, each index represents the number of tests for that count sum

        for n in range(max_n):  # increment n to max_n
            row.append(fn(rand_list[:n]))
            # fn(rand_list[:n]) takes the random list, slices it to n elements and then puts it into fn which
            # is the sorting  algorithm that returns the specified count for the n - list elements
            # This is then appended to the row list

            # To ensure it is still a csv file
            if (n + 1) == max_n:  # if we have reached the last element of the list
                out_file.write(str(row[n]))  # write out the num
            else:
                out_file.write(str(row[n]) + ",")  # write out the num with a comma

        out_file.write("\n")  # write a new line
    out_file.close()  # close the file


if __name__ == '__main__':
    # Unit testing for collect_function_performence_data

    from counting_quad_sorts import bubble_sort  # import  bubble sort for testing purposes

    print("Unit Testing test_function")

    print("\nWriting out data for bubble sort: 7 randomly  lists and 4 number of tests on each \n")
    test_function(bubble_sort, 7, 4) # creating bubble sort test data

    # showing that the test data exists by file io
    file = open(bubble_sort.__name__+".csv",'r')
    print("Reading the bubble sort test data \n" + str(file.readlines())) # displaying it
    file.close()

    import os # importing os inorder to delete the csv file
    os.remove(bubble_sort.__name__+'.csv') # deleting the csv file,
    # incase it may interfer with plotting the actual bubble sort one
