from f_reader import FReader
from f_printer import FPrinter
from pathlib import Path


class IOMgr:
    '''
        The IO manager is used to communicate to the data_printer and
        data_reader classes.  It acts as the manager and interface for
        them.

        .. autoclass::
           :members:

    '''
    def __init__(self, read_path=' ', output_path=' '):
        self.__f_reader = FReader()
        self.__f_printer = DataPrinter()
        self.__read_path = read_path
        self.__output_path = output_path

    def __validate_path(self, path):
        '''
            Validates the path is a Path() object and not just a str object.

            :param path: the path object to be validated
            :type path: Path object
            :raise AttributeError: if path is a str object
            :return: True or False
            :rtype: boolean

        '''
        if path is not str:
            return path.exists()
        else:
            raise AttributeError('str is not a path')

    def __convert_to_path(self, path):
        '''
            Converts str to Path object.

            :param path: The str object to be converted to a Path()
            :type path: str
            :raise Exception: Problem converting to Path
            :return: Path object
            :rtype: Path()

        '''
        try:
            new_path = Path(path)
            return new_path

        except Exception as err:
            return 'Unable to convert str to path, {} {}'.format(
                path, err.__context__)

    def set_read_path(self, path):
        '''
            Sets the read_path.

            :param path: a str to be converted to a path
            :type path: str
            :raise ValueError: if the file path does not exist

        '''
        try:
            self.__read_path = self.__convert_to_path(path)

            if self.__validate_path(self.__read_path) is False:
                raise ValueError('File path does not Exist')

        except Exception as err:
            return 'Input file path invalid: {} {}'.format(
                self.__read_path, err.__context__)

    def set_output_path(self, path):
        '''
            Sets the output path.  This is the path the data will be
            written to.

            :param path: a str to be converted to a path
            :type path: str
            :raise ValueError: if the file path does not exist

        '''
        try:
            self.__output_path = self.__convert_to_path(path)

            if self.__validate_path(self.__output_path) is False:
                raise ValueError('File path does not Exist')

        except Exception as err:
            return 'Error with output file: {}, {}'.format(
                self.__output_path, err.__context__)

    def get_output_path(self):
        '''
        Returns the output path object as a str.

        :return: the output file path
        :rtype: Path()

        '''
        return self.__output_path

    def get_read_path(self):
        '''
        Returns the read file path as a str.

        :return: the csv file to be read.
        :rtype: Path()

        '''
        return self.__read_path

    def read_file(self):
        '''
        Reads data in from file if the file exists.

        :return: a list of potential card holders
        :rtype: list[dict]

        '''
        if self.__read_path != ' ':
            return self.__f_reader.read_file(self.__read_path)
        else:
            raise ValueError('Did not set read path')

    def print_min_file(self, data):
        '''
        Uses the data printer to output data the the output_path.  This prints
        the minimal amount of data for a card holder.

        '''
        if self.__output_path != ' ':
            self.__f_printer.output_min_data_csv(
                self.__output_path, data)
        else:
            raise ValueError('Output file path is blank')

    def print_full_file(self, data):
        '''
        Uses the data printer to print all card holder data to a csv file.

        '''
        if self.__output_path != ' ':
            self.__d_printer.output_full_data_csv(
                self.__output_path, data)
        else:
            raise ValueError('Output file path is blank')
