from f_reader import FReader
import pytest
from pathlib import Path


@pytest.fixture
def default_f_reader():
    dr = FReader()
    return dr


@pytest.fixture
def csv_test_info():
    file_path = Path('test_files/birthdays.csv')
    file_type = 'CSV'
    return (file_path, file_type)
