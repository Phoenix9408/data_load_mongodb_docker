import pandas as pd
import pytest
from src.funct.Projects_variables import  Data_Input_dir, File_name
from src.funct.Data_utility import  Required_data_columns , dtype_med_mapping,columns_dates
from src.funct.Migration_Func import read_data

def test_data_read_func():
    df_origi = pd.read_csv(Data_Input_dir + File_name)
    df_medical = read_data(Data_Input_dir,File_name,dtype_med_mapping,columns_dates)
    df_medical_column  = list(df_medical.columns)
    assert Required_data_columns == df_medical_column
    assert not df_medical.duplicated().any()
    assert len(df_origi) != len(df_medical)
    assert len(df_medical) == 54966

