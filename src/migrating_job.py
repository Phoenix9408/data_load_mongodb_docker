import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.funct.Projects_variables import  Data_Input_dir, File_name, client, Collection
from src.funct.Migration_Func import read_data, migrat_data
from src.funct.Data_utility import  dtype_med_mapping, columns_dates



DF_Medical = read_data(Data_Input_dir,File_name, dtype_med_mapping,columns_dates)

Run = migrat_data(DF_Medical,client,Collection)


