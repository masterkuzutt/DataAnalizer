import pandas as pd 
import numpy as np 

from . import excel
ExcelReader = excel.ExcelReader


class ResourceReader(ExcelReader):
    
    def __init__(self, *args):
        super().__init__()
        self.df = None

    def read(self,**kwarg):
        super().read(**kwarg)
        return True

    def convert_to_df(self,start=None,end=None):
        na = np.array(self.data)
        # self.df = pd.DataFrame(
        #     data=na[1:-1,start:end],
        #     columns=na[0:1,start:end][0],
        #     index=na[1:-1,0:start],
        #     dtype='float32'
        # )
        self.df = pd.DataFrame(
            data=na[1:-1,start:end],
            columns=na[0:1,start:end][0],
            index=pd.MultiIndex.from_arrays(na[1:-1,0:start].T),
            dtype='float32'
        )


        return True
    
    def get_sum(self):
        sum = self.df.sum()
        
        # exclude zero 
        return sum[lambda x : x != 0]
        
    def get_sum_normalize(self):
        
        srs = self.get_sum()
        return (srs - srs.mean()) / (srs.max() - srs.min())
        

