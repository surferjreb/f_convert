"""
 Data Class
 A simple class for holding the data gathered from the file.
 @author: James R. Brown
"""


class FData:

    def __init__(self, data=None):
        self.__data = data

    def set_data(self, new_data):
        """
            Sets some data to the data object
        """
        if new_data is not None:
            self.__data = new_data

    def get_data(self):
        return list(self.__data)

    def __repr__(self):
        return self.__data
