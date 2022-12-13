import functools
import time
import random
from functools import wraps
from matplotlib import pyplot


def sort_timer(func):
    """Decorator function that times the execution time of the decorated function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function to calculate the time taken to execute the sorting function."""
        begin_time = time.perf_counter()  # start time
        func(*args, **kwargs)  # call function
        stop_time = time.perf_counter()  # end time
        return stop_time - begin_time  # return total time

    return wrapper


@sort_timer  # decorating function
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer  # decorating function
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble_sort, insertion_sort):
    """Comparing two sorts method"""
    # x-axis that display num_list in 2,000 increment
    x_coordinates = list()
    # y-axis that display execution time of each sort method in second
    bubble_sort_y_coords = list()
    insertion_sort_y_coords = list()

    # For loop for 10 set of number from 1000 to 10,000 with a step of 1000.
    for num_list_size in range(1000, 10001, 1000):
        # Generate new list of number for each iteration
        num_list_1 = [random.randint(1, 10000) for number in range(num_list_size)]
        print(num_list_1)
        # make a separate copy of list 1
        num_list_2 = list(num_list_1)
        # Assigning time for each bubble sort
        bubble_sort_time = bubble_sort(num_list_1)
        # Assigning time for each insertion sort
        insertion_sort_time = insertion_sort(num_list_2)
        # add list size value to the x-axis
        x_coordinates.append(num_list_size)
        # Assigning time of each sort into their y-column
        bubble_sort_y_coords.append(bubble_sort_time)
        insertion_sort_y_coords.append(insertion_sort_time)

    # Initialize graph for bubble sort
    pyplot.plot(x_coordinates, bubble_sort_y_coords, 'ro--', linewidth=2, label='Bubble sort')
    # Initialize graph for insertion sort
    pyplot.plot(x_coordinates, insertion_sort_y_coords, 'go--', linewidth=2, label='Insertion sort')
    pyplot.xlabel("Num List Size")
    pyplot.ylabel("Execution time in second")
    pyplot.legend(loc="upper left")
    pyplot.show()


compare_sorts(sort_timer(bubble_sort), sort_timer(insertion_sort))
