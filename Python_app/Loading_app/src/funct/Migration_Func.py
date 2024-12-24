import pandas as pd


def read_data(Input_Dir,file, data_type, date_columns):
    Df_Med = pd.read_csv(Input_Dir + file, dtype= data_type, parse_dates=date_columns)
    Df_Med_drop_duplicates = Df_Med.drop_duplicates()
    Df_Med_drop_null_colonne = Df_Med_drop_duplicates.dropna(axis=1, how='all')
    return Df_Med_drop_null_colonne


def migrat_data(med_df,client, collection):
    db = client['ocr']
    collection = db[collection]
    data_dict = med_df.to_dict(orient='records')
    collection.insert_many(data_dict)
    return None