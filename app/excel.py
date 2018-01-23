import xlrd
import os.path 

class DataReader(object):
    """
    this class is base class for data reader class.
     intended to be a baseclass for analyzing array data  
    __init__:
    load():
    read():
    fill_empyt()
    """   
    def __init__(self, *args):
        super().__init__(*args)
        self.data = []
    
    def fill_empty(self, start_col, end_col):
        if self.data :
            for i,line in enumerate(self.data):
                for j  in range(start_col,end_col + 1):
                    if line[j] == '':
                        self.data[i][j] = self.data[i - 1][j] 



class ExcelReader(DataReader):
    """this class just simply Load Excel file and put that data to instance variable.
     intended to be a baseclass for analyzing specific excel data  
    __init__:
    load():
    read():
    """
    def __init__(self,*args):
        """ initialize instance variables"""
        super().__init__(*args)
        self.filepath = None
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



    