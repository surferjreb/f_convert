

class CHParser:
    '''
        Parses the data from the input into a card holder format
    '''

    def get_card(self, card_holder_info):
        try:
            if card_holder_info is not None:
                card = card_holder_info.pop('CardID').split('/')
                return (card[0], card[1], card[2])

            return
        except KeyError as err:
            tb = err.__traceback__
            raise KeyError('CardID Missing').with_traceback(tb) from err

    def get_card_holder_name(self, card_holder_info):
        try:
            if card_holder_info is not None:
                return (card_holder_info.pop('LastName'),
                        card_holder_info.pop('FirstName'),
                        card_holder_info.pop('MiddleName'))

            return
        except KeyError as err:
            tb = err.__traceback__
            raise KeyError('Missing Key').with_traceback(tb) from err

    def get_card_holder_data(self, card_holder_data):
        temp_data = {}

        if card_holder_data is not None:
            for value in card_holder_data:
                temp_data[value] = card_holder_data[value]

        return temp_data
