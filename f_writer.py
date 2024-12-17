

class FWriter:

    def __init__(self, data):
        self.data = data

    def write_file(self, output_path, output_type='CSV'):
        '''
            Writes data to output path as output_type.
        '''
        try:
            is_created = False
            match self.__output_type:
                case 'CSV':
                    is_created = self.write_csv(self.__output_path)

                case 'JSON':
                    pass

                case 'XML':
                    pass

                case _:
                    'Not a selection'

            if is_created:
                return 'File saved to: {}'.format(str(self.__output_path))

        except Exception as err:
            raise Exception('Failed to write', err.__context__)

    def __write_csv(self, output_path):
        try:
            with open(output_path, 'w') as out_file:
                for item in self.data:
                    if self.data.index(item) == 0:
                        for key in self.data.keys():
                            if key.next() != None:
                                out_file.write(key, ',')
                            else:
                                out_file.write(key, '\n')
                    else:
                        for key in self.data.keys():
                            if key.next() != None:
                                out_file.write(self.data.get(key), ', ')
                            else:
                                out_file.write(self.data.get(key), '\n')

        except Exception as err:
            raise Exception('Failed CSV', err.__context__)

    def __write_json(self, output_path):
        pass

    def __write_xml(self, output_path):
        pass

    # change output_type
    # change output path


