
# -*- coding: utf-8 -*-

import os.path 

import pandas as pd 
import numpy as np 
import xlrd


class DataReader(object):
    """
    this class is base class for data reader class.
    ‐ __init__:
    - fill_empyt()
    """   

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def data(self):
        return self._data 
    
    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = value 
        else: 
            raise ValueError (' value is not "list"')

    def fill_empty(self, start_col, end_col):
        # [TODO] move to helper class 
        for i,line in enumerate(self._data):
            for j  in range(start_col,end_col + 1):
                if line[j] is None or line[j] == '':
                    # print("----", self._data[i][j], self._data[i - 1][j])
                    self._data[i][j] = self._data[i - 1][j] 


class ExcelReader(DataReader):
    """
    this class just simply Load Excel file and put that data to instance variable.
     intended to be a baseclass for analyzing specific excel data  
    - __init__:
    - load():
    - read():
    """

    def __init__(self,*args):
        """ initialize instance variables"""
        super().__init__(*args)
        self.filepath = None
        self.xls = None

    def load(self,filepath):
        """ load excel file object to self.xls""" 
        
        self.filepath=filepath
        
        if isinstance(self.filepath,str) != True:
            return False
        
        elif os.path.isfile(self.filepath) != True:
            raise FileNotFoundError ("'{}' not found".format(self.filepath))

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

        self.data = np.zeros((nrows, ncols)).tolist()
 
        for r in range(nrows):
            for c in range(ncols):
                if st.cell(r,c).value:
                    self.data[r][c] = st.cell(r,c).value
                else:
                    self.data[r][c] = None
        return True


# [TODO] looks weird. excel is one of  resources
class ResourceReader(ExcelReader):
    
    def __init__(self, *args):
        super().__init__()
        self.df = None

    def convert_to_df(self,start=None,end=None):
        na = np.array(self.data)

        self.df = pd.DataFrame(
            data=na[1:-1,start:end],
            columns=na[0:1,start:end][0],
            index=pd.MultiIndex.from_arrays(na[1:-1,0:start].T)
            #,dtype='float32'
        )

        return True
    
    def get_sum(self):
        sum = self.df.sum()
        
        # exclude zero 
        return sum[lambda x : x != 0]
        
    def get_sum_normalize(self):
        
        srs = self.get_sum()
        return (srs - srs.mean()) / (srs.max() - srs.min())
        

