import unittest


import app.excel as xls
import app.analyzer as az

import numpy as np
import pprint


class TestExcel(unittest.TestCase):

    def setUp(self):
        self.xls = xls.ExcelReader()

    def tearDown(self):
        pass
    
    def test_load(self):
        pass

    def test_read(self):
        filepath = r"tests\test.xlsx" 
        self.xls.load(filepath)
        self.assertTrue(self.xls.read())
        self.assertTrue(self.xls.read(sheet_name="評価シート"))
        # for ln in self.xls.data:
        #     print(ln)

class TestAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.xls = az.ResourceReader()

    def tearDown(self):
        pass
    
    def test_load(self):
        
        pass

    def test_read(self):
        filepath = r"tests\test.xlsx" 
        self.xls.load(filepath)
        self.assertTrue(self.xls.read())

        self.assertTrue(self.xls.read(sheet_name="評価シート"))
        self.assertTrue(self.xls.convert_to_df(start=3,end=36))
        print(self.xls.get_sum_normalize())