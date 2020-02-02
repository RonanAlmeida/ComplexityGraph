"""
This Module is used for calculating the column averages for the test data.
it does it by first reading the file and appending each column to a list, calculating the average of that list
and then appending those to a list of column averages.

Author: Ronan Almeida
Student Num: 20178025
Date: 2019-15-11
"""


def get_file_column_averages(filename):
    """
    this function given the filename- calculates the column averages. It does this by reading filename
    parsing it into a 2d list of floats then calculating each column average and appending it to a
    separate list

    Parameters:
        filename - a csv file in which contains test data for various sorting passes

    Returns:
        colavg_list - a list of all the column averages in filename
    """

    filename = open(filename, 'r')  # open the file for reading

    lines = filename.read().strip().split(
        '\n')  # strip the filename, and split by each new line into the 2d list'lines'
    filename.close()  # close the file

    list_num = []  # define list_num - a 2d list of all the numbers in filename as an int
    currentline = []  # current line - a list of the current line of 'lines' split by commas

    for x in range(len(lines)):  # increment x up to the number of lines
        currentline.append(lines[x].split(','))  # append the current line split by commas
        list_num.append([])  # add an empty list for the 2d list

        for y in range(len(currentline[x])):  # for y up to the number of elements in the current line
            list_num[x].append(int(currentline[x][y]))  # append each element of current line to list_num as an int

    colavg_list = []  # a list of all the column averages
    for y in range(len(list_num)):  # Since we're calculating the column averages  start with y (helps understanding)

        col_sum = 0  # the sum

        for x in range(len(list_num)):  # for each x going down the column of list_num
            col_sum += list_num[x][y]  # add that column element to the col_sum

        colavg_list.append(round(col_sum / len(list_num))) # calculate the average using round and append to the list

    return colavg_list # return the list of all column averages

if __name__ == '__main__':
    # Unit testing for file column_averages

    print("\nUnit testing for get_file_column_averages\n")

    import  collect_function_performance_data
    from counting_quad_sorts import bubble_sort

    collect_function_performance_data.test_function(bubble_sort, 5, 5) # creating bubble sort test data

    # showing that the test data exists by file io
    file = open(bubble_sort.__name__+".csv",'r')
    print("Creating Bubble Sort Data \n" + str(file.readlines())) # displaying it
    file.close()

    avg_col = get_file_column_averages(bubble_sort.__name__+".csv") # calculating averages
    print("\n\nHere are the averages for the columns of that bubble sort data \n" + str(avg_col))

    import os # importing os inorder to delete the csv file
    os.remove(bubble_sort.__name__+'.csv') # deleting the csv file,
    # in case it may interfer with plotting the actual bubble sort one
