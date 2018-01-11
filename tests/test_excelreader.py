import unittest 
import app.excel as xls


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
        print(self.xls.data)