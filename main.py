import f_convert


FILE = 'test_files/colors2.json'

def main():
    converter = f_convert.FConvert(FILE)
    converter.convert_to_csv()


if __name__ == '__main__':
    main()
