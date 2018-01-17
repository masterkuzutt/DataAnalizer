from app.excel import ExcelReader
import pandas as pd 
import numpy as np 


class ResourceReader(ExcelReader):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.df = None

        
    def read(self,**kwarg):
        super().read(**kwarg)
        self.data = np.array(self.data)
        return True

    def convert_to_df(self,start=None,end=None):
        self.df = pd.DataFrame(
            data=self.data[1:-1,start:end],
            columns=self.data[0:1,start:end][0],
            index=self.data[1:-1,0:start],
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
        

