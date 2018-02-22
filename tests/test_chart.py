import os
import unittest
import glob

from app.chart import Chart 

class TestDataReader(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
            

    def test_data_setter(self):
        pass


from app.chart import RadarChart 

class TestDataReader(unittest.TestCase):
    
    @classmethod       
    def setUpClass(cls):
        filepath  = os.sep.join(["tests","output","*"] )
        [ os.remove(f) for f in glob.glob(filepath)  ]

    def setUp(self):
        self.name_list = ["name_a", "name_b"] 
        self.values_list = [[0.3, 0.4, 0.5, 0.6, 0.3],
                            [0.9, 0.1, 0.7, 0.6, 0.6]] 
        self.categories = ["A","B","C","D","E"] 
        self.rc = RadarChart(self.name_list,self.values_list,self.categories)

    def tearDown(self):
        pass

    @classmethod       
    def tearDown(cls):
        pass

    def test_create_chart_nonsave(self):
        # [TODO]
        pass
        # self.rc.create_chart()
        # chart should apear

    def test_create_chart_save(self):
        dirpath = "tests" + os.sep + "output"
        filename="test.png"
        
        self.rc.save = True
        self.rc.dirpath = dirpath
        self.rc.filename= filename
    
        self.rc.create_chart()
        self.assertTrue(os.path.exists(os.sep.join([dirpath,filename])))

        # chart should apear

