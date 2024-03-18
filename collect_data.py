# File modeled after https://github.com/scienceltrs/SciPub/blob/main/authors.py
import pandas as pd
import csv

from pathNames import path_2023w1, path_2023s2, path_2023s1, path_2023s12, path_2022w2, path_2022w1, path_2022w12, path_2022s2, path_2022s1, path_2022s12, mt_output_path, fe_output_path  

is_collecting_midterm_data = True

MT_LT_COLUMN_NAME    = 'MT LT'
MT_INVIG_COLUMN_NAME = 'MT Invig LT'
FE_LT_COLUMN_NAME    = 'FE LT'
FE_INVIG_COLUMN_NAME = 'FE Invig LT'

class DataPair:


    def __init__(self, lt_used, invig_used):
        self.lt_used = lt_used
        self.invig_used = invig_used

    def __eq__(self, other):
        return isinstance(other, DataPair) and self.lt_used == other.lt_used and self.invig_used == other.invig_used
    

    def __hash__(self) -> int:
        return 1


#def get_column_name(column_type, data):
#    if (not isinstance(column_type, str) or not isinstance(data, pd.DataFrame)):
#        raise TypeError(f"Incorrect parameter type. Must be get_column_name(str, pd.DataFrame). Actual types are {type(column_type)}., {type(data)})")
#    while True:
#        column_name = input(f"Please enter the name of the {column_type} column: ")
#        if column_name in data.columns :
#            return column_name
#        else:
#            print("The column name entered does not appear in the CSV. Please try again.")
    

def generate_data(pair_dict, data_path):

    data = pd.read_csv(data_path)
    if is_collecting_midterm_data:
        if not (data.columns.__contains__(MT_LT_COLUMN_NAME) and data.columns.__contains__(MT_INVIG_COLUMN_NAME)):
            print("Warning: Incomplete midterm columns in " + data_path)
            return pair_dict
        lt_column_name    = MT_LT_COLUMN_NAME   
        invig_column_name = MT_INVIG_COLUMN_NAME
    else:   # when collecting final exam data
        if not (data.columns.__contains__(FE_LT_COLUMN_NAME) and data.columns.__contains__(FE_INVIG_COLUMN_NAME)):
            print("Warning: Incomplete final exam columns in " + data_path)
            return pair_dict
        lt_column_name    = FE_LT_COLUMN_NAME   
        invig_column_name = FE_INVIG_COLUMN_NAME
    exam_info_data = data[[lt_column_name,invig_column_name]].dropna()

    for index, row in exam_info_data.iterrows():
        class_exam_lt = row[lt_column_name]
        class_exam_invig = row[invig_column_name]
        data_pair = DataPair(class_exam_lt, class_exam_invig)
        if data_pair in pair_dict:
            pair_dict[data_pair] += 1
        else:
            pair_dict[data_pair] = 1
    
    return pair_dict

def write_file(output_path, data_dict):
    with open(output_path, 'w', newline = '' ) as file:
        writer = csv.writer(file)
        field = ["LT Used", "Invig Used", "Count"]
        writer.writerow(field)
        for data_pair, count in data_dict.items():
            writer.writerow([data_pair.lt_used, data_pair.invig_used, count])

def generate_all_data(output_path):
    pair_dict = {}
    
    generate_data(pair_dict ,path_2022s1)
    generate_data(pair_dict ,path_2022s2)
    generate_data(pair_dict ,path_2022s12)
    generate_data(pair_dict ,path_2022w1)
    generate_data(pair_dict ,path_2022w2)
    generate_data(pair_dict ,path_2022w12)
    generate_data(pair_dict ,path_2023w1)
    generate_data(pair_dict ,path_2023s1)
    generate_data(pair_dict ,path_2023s2)
    generate_data(pair_dict ,path_2023s12)

    write_file(output_path, pair_dict)

def main():
    global is_collecting_midterm_data
    is_collecting_midterm_data = True
    generate_all_data(mt_output_path)
    is_collecting_midterm_data = False
    generate_all_data(fe_output_path)

if __name__ == "__main__":
    main()