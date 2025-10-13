class budget:
    def __init__(self, name, estimate, actual):
        self.__estimate = float(estimate)
        self.__actual = float(actual)
        self.__difference = float
        self.__name = (name)
    
    def diff_calc(self):
        self.__difference = self.__actual - self.__estimate
        

class expense(budget):
    def __init__(self, name, estimate, actual):
        super().__init__(name, estimate, actual)
    
#    def diff_calc(self):
#        self.__difference = self.__actual - self.__estimate
        