from bs4 import BeautifulSoup 
import csv
import os
from .utils import create_dir_if_not_exists
from .ns import DATA_DIRECTORY


class HtmlHandler:
    def extract(self, new_path: str, data_type: str) -> list:
        try:
            self._read_new_file(new_path)
        except:
            print(f"Unable to read {new_path}")
        self._update_set_from_old_file(data_type)
        self._update_db_data(data_type)
        return self.clean_list

    def _read_new_file(self, new_data_path: str):
        with open(new_data_path, "r") as HTMLFile:
            index = HTMLFile.read() 
            Parse = BeautifulSoup(index, 'html') 
            elements = Parse.find_all('div')
            output = []

            for div in elements:
                a = div.find_all('a')
                text = [i.text for i in a]
                output += text
            self.clean_list = list(set(output))
        print(f"INFO {len(self.clean_list)} inserted from {self.new_data_path}")
    
    def _update_set_from_old_file(self, data_type: str):
        db_data_path = f"{DATA_DIRECTORY}{data_type}.csv"
        if not os.path.isfile(db_data_path):
            print(f"WARNING no old file: {db_data_path}")
            return
        with open(db_data_path, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
        clean_list = list(set([element[0] for element in data])) + self.clean_list
        self.clean_list = clean_list
    
    def _update_db_data(self, data_type):
        create_dir_if_not_exists(DATA_DIRECTORY)
        db_data_path = f"{DATA_DIRECTORY}{data_type}.csv"
        with open(db_data_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows([[r] for r in self.clean_list])