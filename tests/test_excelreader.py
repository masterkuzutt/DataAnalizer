import unittest

import numpy as np
import pprint

import app.excel as xls
import app.analyzer as az


class TestDataReader(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
            
    def test_fill_empty(self):
        dr = xls.DataReader()
        dr.data = [[1,2,3,4],["","","",""],[5,6,7,8]]
        dr.fill_empty(0,1)
        self.assertEqual(dr.data[1].count(""),2)


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
    
    def test_fill_empty(self):
        pass