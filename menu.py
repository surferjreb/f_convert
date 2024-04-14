import pyfiglet
import sys
from simple_term_menu import TerminalMenu


_menu_title = '''
    ******************************************************************
    ******************************************************************
    **                                                              **
    **                         CSV Rudby                            **
    **                      By: James R Brown                       **
    **                        License: MIT                          **
    **                                                              **
    ******************************************************************
    ******************************************************************
'''


class Menu:
    def __init__(self, manager):
        self._title = 'CSV Rudby'
        self.selection = None
        self.menu_selections = ['Read CSV file',
                                'Show Card holders',
                                'Export Card Holders',
                                'Export All Card holders data',
                                'Edit Card Holders',
                                'Exit'
                                ]
        self.manager = manager

    def get_title(self):
        f = pyfiglet.figlet_format(self._title, font='small_slant')
        print(f)
        print(_menu_title)

    def start_menu(self):
        tmenu = TerminalMenu(self.menu_selections)

        self.get_title()

        selection = tmenu.show()

        while selection != 5:
            self.get_menu_selection(selection)
            selection = tmenu.show()

        print('GoodBye!')
        sys.exit()

    def get_menu_selection(self, selection):
        if selection is not None:

            match selection:
                case 0:
                    self.read_csv()
                case 1:
                    self.display_card_holders_simple()
                case 2:
                    self.output_min_ch_to_csv()
                case 3:
                    print('Edit Card Holders')
                case _:
                    print('Try again....!')

    def read_csv(self):
        try:

            if self.manager.get_read_path() == ' ':
                file_path = input("Please enter file location: ")
                self.manager.set_read_path(file_path)

            self.manager.read_csv()
            print('Read Complete\n')
        except Exception as err:
            print('Error reading file: {}, {}'.format(
                self.manager.get_read_path(), err.__context__ ))

    def display_card_holders_simple(self):
        card_holders = self.manager.get_card_holders()

        if card_holders is not None:
            for holder in card_holders:
                print(holder)

    def output_min_ch_to_csv(self):

        if self.manager.get_output_path() == ' ':
            file_path = input('Please enter a file path to save csv to: ')
            self.manager.set_output_path(file_path)

            self.manager.output_min()
