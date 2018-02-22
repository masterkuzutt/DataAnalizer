import os 
import glob

import pandas as pd 
import numpy as np 

from .datareader import ResourceReader

def create_df(filepath,sheetname, stert_col, end_col):
    data_reader = ResourceReader()
    data_reader.load(filepath)
    data_reader.read(sheet_name=sheetname)
    data_reader.convert_to_df(stert_col, end_col)
    return data_reader.df

def create_df_from_dir(dirpath, sheetname, stert_col, end_col):

    print("------------")
    file_list = glob.glob(dirpath)

    df = pd.DataFrame()

    for filepath in file_list:
        if df.empty:
            print("empty")  
        filename = os.path.basename(filepath)
        
    return df 


def df_to_chartdata():
    pass

def run():
    pass

def main():
    dirpath=r"C:\Users\t_sakai\Documents\python\testenv\danalyzer\tests\input\*.xlsx"
    sheetname="sheet1"
    s = 3
    e = 20

    create_df_from_dir(dirpath, sheetname, s ,e )
