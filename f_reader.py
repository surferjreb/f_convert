import csv
from f_data import FData


class FReader:
    '''
        Reads the file data into the program.  This data then can be
        converted(future).

        .. autoclass:: FReader
           :members:

    '''
    FILE_TYPE = {1: "CSV", 2: "JSON", 3: "XML"}

    def __init__(self):
        self.__data = []

    def file_read(self, file_path, file_type='CSV'):
        '''
            This method begins the process of reading the data into the
            program.  Default file_type is csv, unless specified.

            :param file_path:
            :type file_path: Path()
            :raise Exception: raises the value that causes the exception
            :return: returns a list of dict values
            :rtype: list[dict]

        '''
        try:
            tempList = []

            match file_type:
                case 'CSV':
                    tempList = self.__read_csv(file_path)
                case 'JSON':
                    tempList = self.__read_json(file_path)
                case 'XML':
                    tempList = self.__read_xml(file_path)
                case _:
                    return 'Selection is not specified'

            if tempList is not None:
                self.__data = list(tempList)

        except Exception as err:
            return 'Unable to read, {}, {}'.format(err.__context__,
                                                   err.__cause__)

    def __read_csv(self, file_path):
        temp_list = []

        try:
            with open(file_path, 'r') as f:
                temp_data = csv.DictReader(f)

                for row in temp_data:
                    temp_list.append(row)

                return temp_list

        except Exception as err:
            raise Exception(err.__class__, err.__cause__) from err

    def __read_json(self, file_path):
        #TODO: Finish writing method
        print('Reading JSON file!')

    def __read_xml(self, file_path):
        #TODO: Finish writing method
        pass

    def get_data(self):
        return list(self.__data)

    def __repr__(self):
        return '{}'.format(self.__class__)
