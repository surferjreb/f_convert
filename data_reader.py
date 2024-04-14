import csv


class DataReader:
    '''
        Reads the csv into the program
    '''
    def __init__(self):
        pass

    def read_file(self, file_path):
        '''
            Reads the file from the file_path provided.  It then sends this
            information the create_card_holder, this returns a card_holder
            object which is passed to add_card_holder method.

            :raise Exception: raises the value that causes the exception
            :return: returns a list of dict values
            :rtype: list[dict]

        '''
        temp_list = []

        try:
            with open(file_path, 'r') as f:
                temp_data = csv.DictReader(f)

                for row in temp_data:
                    temp_list.append(row)

                return temp_list

        except Exception as err:
            raise Exception(err.__class__, err.__cause__) from err

    def __repr__(self):
        return '{}'.format(self.__class__)
