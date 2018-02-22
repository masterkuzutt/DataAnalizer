import os
import unittest
import glob

import pandas as pd 
import numpy as np 

from app import *

class TestApp(unittest.TestCase):

    def setUp(self):
        self.dirpath="input"        
        self.filepath=r"tests\input\test.xlsx"
        self.sheetname="sheet1"
        self.start_col = 3
        self.end_col = 20

    def tearDown(self):
        pass
            
    def test_create_df(self):
        result = create_df(self.filepath, self.sheetname, self.start_col, self.end_col)
        self.assertTrue(isinstance(result,pd.DataFrame))
        
    def test_create_df_from_dir(self):
        # result = create_df_from_dir(self.dirpath, self.sheetname, self.start_col, self.end_col)
        pass

    def test_create_chart(self):
        pass    


