"""Module providing a ListAverager class."""
from functools import reduce


class ListAverager:
    """Class representing a ListAverager"""

    @staticmethod
    def list_average(num_list):
        """Function return average of list elements."""
        return reduce(lambda a, b: a + b, num_list) / len(num_list)

    def comp_averages(self, first_list, second_list):
        """The function returns a string comparing the average values of list elements."""
        first_list_average = self.list_average(first_list)
        second_list_average = self.list_average(second_list)

        if first_list_average == second_list_average:
            return 0
        if first_list_average > second_list_average:
            return 1
        return -1
