"""
This module is basically the  structure of the user interface
in which other modules and functions interact within the menu/choices to deliver
the user experience. The main() function is the entry of the program's execution.


Author: Ronan Almeida
Student Number: 20178025
Date: 2019-15-11
"""

# import all functions for use
import collect_function_performance_data
import counting_quad_sorts
import file_chooser
import file_column_averages
import menu
import plotter

# Constants
MAX_N = 100  # Maximum length of randomly generated lists
NUM_TESTS = 100  # Number of tests to run on each chosen sort


def main():
    while True:  # main menu while loop
        # Do menu choices
        user_choice = menu.do_menu("Main Menu", ["Generate sort time files", "Plot average sort times"])
        if user_choice is None:
            break  # exit choice

        print('\nValid choice:', user_choice)

        if user_choice == 1:  # first menu choice - generate tests
            while True:  # Sub menu
                user_choice = menu.do_menu("Select a sort",
                                           ["Bubble sort",
                                            "Insertion Sort",
                                            "Optimized bubble sort",
                                            "Selection sort"])
                if user_choice is None:
                    break  # exit choice
                print('\nValid choice:', user_choice)

                if user_choice == 1:  # Generating test files  for bubble sort
                    # Calling the data test function to generate the csv file
                    print("\nGenerating test files.. for " + counting_quad_sorts.bubble_sort.__name__)
                    collect_function_performance_data.test_function(counting_quad_sorts.bubble_sort, MAX_N, NUM_TESTS)
                    print("\n" + counting_quad_sorts.bubble_sort.__name__ + ".csv generated")


                elif user_choice == 2:  # Generating test files  for insertion sort
                    # Calling the data test function to generate the csv file
                    print("\nGenerating test files.. for " + counting_quad_sorts.insertion_sort.__name__)
                    collect_function_performance_data.test_function(counting_quad_sorts.insertion_sort, MAX_N,
                                                                    NUM_TESTS)
                    print("\n" + counting_quad_sorts.insertion_sort.__name__ + ".csv generated")

                elif user_choice == 3:  # Generating test files for optimized bubble sort
                    # Calling the data test function to generate the csv file
                    print("\nGenerating test files.. for " + counting_quad_sorts.opt_bubble_sort.__name__)
                    collect_function_performance_data.test_function(counting_quad_sorts.opt_bubble_sort, MAX_N,
                                                                    NUM_TESTS)
                    print("\n" + counting_quad_sorts.opt_bubble_sort.__name__ + ".csv generated")


                elif user_choice == 4:  # Generating test files for selection sort
                    # Calling the data test function to generate the csv file
                    print("\nGenerating test files.. for " + counting_quad_sorts.selection_sort.__name__)
                    collect_function_performance_data.test_function(counting_quad_sorts.selection_sort, MAX_N,
                                                                    NUM_TESTS)
                    print("\n" + counting_quad_sorts.selection_sort.__name__ + ".csv generated")



        elif user_choice == 2:  # 2nd menu choice plot average sort times
            # n num of choices
            while True:  # Sub menu
                file_path = file_chooser.get_file_path_and_name(pattern='*.csv')  # file_path is a list of the csv files
                if file_path is None:
                    break  # exit choice

                if file_path != None:  # if there exists a file(s) in file_path
                    print('Path:', file_path[0])  # display its path
                    print('File:', file_path[1])
                    print('Both:', file_path[0] + "\\" + file_path[1])
                    print("\nCalculating Averages for " + file_path[1])

                    # Calculates the column averages for that particular csv file
                    col_avg = file_column_averages.get_file_column_averages(file_path[1])

                    print("\n Plotting Graph: " + file_path[1][:len(file_path[1]) - 4])

                    # Plotting the graph of the averages

                    # Setting up graph
                    plot_graph = plotter.plot(title=file_path[1][:len(file_path[1]) - 4],
                                              origin_x=15,
                                              origin_y=15,
                                              scale_x=6,
                                              scale_y=0.11,
                                              bg='darkseagreen1')

                    plot_graph['draw_axes'](tick_length=4, tick_interval_y=100)  # set up axes

                    # Plot each point by for loop
                    for x in range(len(col_avg)):
                        plot_graph['plot_point'](x, col_avg[x], 6
                                                 , colour='red')  # color red

                    # the n^2/2 function, commented out
                    # plot_graph['plot_function'](lambda x: (x ** 2) / 2 if x >= 0 else None)
                    # plot_graph['put_text']('T(n) = n^2/2', x=70, y=150, size=12, colour='black')

                    # Labels T (100s), n, legend, t(n) = filename
                    plot_graph['put_text']('T\n(100s)', 2, 5500, size=9, colour='Black')
                    plot_graph['put_text']('n', 100, 100, size=9, colour='Black')
                    plot_graph['put_text']('Legend:', x=70, y=450, size=12, colour='blue')
                    plot_graph['put_text']('T(n) = ' + file_path[1][:len(file_path[1]) - 4], x=70, y=300, size=12,
                                           colour='red')

                    plot_graph['block']()  # Module exits when user closes the canvas window.


main()



if __name__ == '__main__':
    print("Unit testing a4\n This is all print statements and while loops/menus ")
