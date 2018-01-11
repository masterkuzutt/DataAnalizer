import xlrd
import os.path 
import numpy as np

class ExcelReader(object):
    def __init__(self):
        self.filepath = None
        self.data = []
        self.xls = None

    def load(self,filepath):
        if isinstance(filepath,str) != True:
            return False
        elif os.path.isfile(filepath) != True:
            return False
        elif filepath.endswith('xlsx') != True :
            return False
        
        self.xls = xlrd.open_workbook(filepath)
        return True


    def read(self, sheet_index=0):
        
        st = self.xls.sheet_by_index(sheet_index)
        nrows = st.nrows
        ncols = st.ncols 

        self.data = [[0 for i in range(ncols)] for j in range(nrows)]

        for r in range(nrows):
            for c in range(ncols):
                self.data[r][c] = st.cell(r,c).value
        return True

          