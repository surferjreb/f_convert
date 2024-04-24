from pathlib import Path
from f_reader import FReader

class TestFReader:
    '''
        Test class for f_reader
    '''

    def test_default_class(self, default_f_reader):
        '''
            Tests that the class can be instantiated.
        '''
        dr = default_f_reader
        assert dr is not None

    def test_read_f(self, default_f_reader, csv_test_info):
        '''
            Tests that the class reads in a file and updates the class list.
        '''
        r = default_f_reader
        r.file_read(csv_test_info[0])
        data = r.get_data()
        assert len(data) >= 1

    def test_read_return_empty(self, default_f_reader):
        '''
            Tests that the class attempts to read the non-existant file.  Then
            returns a empty list or an object of zero length.
        '''
        dr = default_f_reader
        dr.file_read(Path('test_files/test.csv'))
        data = dr.get_data()
        assert len(data) == 0
