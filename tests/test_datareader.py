import os
import unittest

import numpy as np
import pprint

from app.datareader import DataReader 
class TestDataReader(unittest.TestCase):

    def setUp(self):
        self.dr = DataReader()
        self.dr.data = [[1,2,3,4],["","","",""],[5,6,7,8]]

    def tearDown(self):
        pass
            
    def test_data_setter(self):
        self.assertEqual(np.shape(self.dr.data),(3,4))

    def test_fill_empty(self):
        self.dr.fill_empty(0,1)
        self.assertEqual(self.dr.data[1].count(""),2)


from app.datareader import ExcelReader 
class TestExcel(unittest.TestCase):

    def setUp(self):
        self.xls = ExcelReader()
        filename = r"test.xlsx" 
        dirpath = r"tests\input"
        self.filepath = os.sep.join([dirpath,filename])

    def tearDown(self):
        pass

    
    def test_load(self):
        print(self.filepath)
        self.assertEqual(True, self.xls.load(self.filepath))

    def test_read(self):
        self.xls.load(self.filepath)
        self.assertTrue(self.xls.read())
        self.assertEqual(np.shape(self.xls.data),(2, 3))

    def test_read_sheetname(self):
        self.xls.load(self.filepath)
        self.assertTrue(self.xls.read(sheet_name="sheet1"))
        self.assertEqual(np.shape(self.xls.data),(61, 38))
    

from app.datareader import ResourceReader 
class TestAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.xls = ResourceReader()
        self.filename = "test.xlsx" 
        self.dirpath = "tests" + os.sep + r"input"
        self.filepath = os.sep.join([self.dirpath,self.filename])

    def tearDown(self):
        pass


    def test_load(self):        
        self.assertTrue(self.xls.load(self.filepath))
    
    def test_load_nonexist_path(self):
        path = "notexistpath.xlsx"
        self.assertRaises(FileNotFoundError, lambda:self.xls.load(path) )

    def test_load_not_string(self):        
        # file not exist 
        path = 123
        self.assertFalse( self.xls.load(path) )

    def test_load_wrong_extention(self):        
        # file should be exist
        path = r"test.txt"
        self.assertFalse( self.xls.load(os.sep.join([self.dirpath, path])) )


    def test_read(self):
        self.xls.load(self.filepath)
        self.assertTrue(self.xls.read())

    def test_convert(self):
        self.xls.load(self.filepath)
        self.assertTrue(self.xls.read(sheet_name="sheet1"))
        self.assertTrue(self.xls.convert_to_df(start=3,end=36))
    
   
