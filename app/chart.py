# -*- coding: utf-8 -*-

import os 
from math import pi

import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryo.ttc', size=10)



class Chart(object):

    def __init__(self, name_list, values_list, categories):
        """
        constructor for chart
        Args:
            name_list: list string for radar chart name.
            values_list: value 2d list for plot data.
                        len(1D should be same with name.len(2D) should be same with categories.
            categories:categoies name for chart x axis .
        """
        super().__init__()
        self.name_list = name_list
        self.values_list = values_list
        self.categories = categories
    
    def create_chart(self):
        """
        create chart and show
        """
        self._create_angles()
        self._initialize_plt()           
        self._produce_chart()
      
    def _create_angles(self):
        raise NotImplementedError

    def _initialize_plt(self):
        raise NotImplementedError

    def _produce_chart(self):
        raise NotImplementedError


class RadarChart(Chart):
    
    def _create_angles(self):
        """
        create angle for radar chart
        
        Returns:
            bool:The return value. True for success
        """
        N = len(self.categories)
        self.angles = [n / float(N) * 2 * pi for n in range(N)]
        self.angles += self.angles[:1]
        return True

    def _initialize_plt(self):
        """
        initialize matplotlib.pyplot.create xtricks, yticks,ylim
        if should be called after _create_angles()  

        Returns:
            bool:The return value. True for success,false if self.anges is empty.
        """

        if not self.angles:
            return False
        
        # cloase old session 
        plt.close()
        self.ax = plt.subplot(111, polar=True)
        
        # # set title
        plt.xticks(
            self.angles[:-1], 
            self.categories, 
            color='grey', 
            size=8, 
            fontproperties=fp)
        ytick_angle = [ float("0." + str(x) ) for x in range(1,10) ] 
        ytick_label = [ str(x) for x in range(10,100,10) ]
        plt.yticks(ytick_angle, ytick_label , color="grey", size=7)
        plt.ylim(0,1)       
        return True


    def _produce_chart(self):
        """
        produce chart data 
        Returns:
            bool:The return value. True for success,false otherwise
        """ 
        try:
            for name,values in zip(self.name_list,self.values_list):        
                # # # Plot data
                values += values[:1]
                self.ax.set_rlabel_position(0)
                self.ax.plot(self.angles, values, linewidth=1, linestyle='solid')
                # # # Fill area        
                self.ax.fill(self.angles, values, 'b', alpha=0.1)
            
            # plt.legend(self.name_list,prop=fp,bbox_to_anchor=(0.9, 1.0, 0.5, .100))
            plt.legend(self.name_list,prop=fp,bbox_to_anchor=(-0.02, 1.0))
            
            # [TODO] looks ugly.need to refactor
            if hasattr(self,"save") and self.save:
                filepath = os.sep.join([self.dirpath,self.filename])
                plt.savefig(filepath)

            else:
                plt.show()

        except:
            # print("--------in-------")
            raise 
            return False
        else:
            return True

