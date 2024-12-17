from dotenv import load_dotenv
import json, csv


load_dotenv()


class FConvert:
    def __init__(self, file=None):
        self.file = file
        self.temp_data = None

    #TODO: write func to convert csv to JSON
    def convert_to_json(self):
        with open(self.file) as file:
            csv_data = csv.DictReader(file)
            self.temp_data = list(csv_data)

        json_data = json.dumps(self.temp_data, indent=4)

        with open('csvtojson.json', 'a') as file:
            file.write(json_data)

        self.temp_data = None

    #TODO write func to convert JSON to csv
    def convert_to_csv(self):
        with open(self.file) as file:
            json_data = json.load(file)
            self.temp_data = json_data

        headers = self.temp_data[0].keys()
        with open('jsontocsv.csv', 'a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.temp_data)

        self.temp_data = None