import xlrd
import os.path 

class ExcelReader(object):
    """this class just simply Load Excel file and put that data to instance variable.
     intended to be a baseclass for analyzing specific excel data  
    __init__:
    load():
    read():
    """
    def __init__(self):
        """ initialize instance variables"""
        self.filepath = None
        self.data = []
        self.xls = None

    def load(self,filepath):
        """ load excel file """ 
        self.filepath=filepath
        if isinstance(self.filepath,str) != True:
            return False
        elif os.path.isfile(self.filepath) != True:
            return False
        elif self.filepath.endswith('xlsx') != True :
            return False
        
        self.xls = xlrd.open_workbook(self.filepath)
        return True


    def read(self, sheet_index=0,sheet_name=None):
        """read specified sheet to self.data as a 2D array"""
        try:
            if sheet_name :
                st = self.xls.sheet_by_name(sheet_name)
            else:            
                st = self.xls.sheet_by_index(sheet_index)
        except:
            pass
            # [TODO] implement error handling 

        nrows = st.nrows
        ncols = st.ncols 

        self.data = [[0 for i in range(ncols)] for j in range(nrows)]

        for r in range(nrows):
            for c in range(ncols):
                self.data[r][c] = st.cell(r,c).value
        return True


