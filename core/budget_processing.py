class budget:
    def __init__(self, name, estimate, actual, current_balance):
        self.__estimate = float(estimate)
        self.__actual = float(actual)
        self.__difference = 0
        self.__name = (name)
        self.__current_balance = float(current_balance) #should this be manually asked per session? Or can I find a way to automatically call this from user's banks?
        
    def diff_calc(self):
        self.__difference = self.__actual - self.__estimate
        return self.__difference
    
    def savings():
        #take the difference of expense and income to show how much should be in the user's savings.
    
    def average_savings():
        #take incomes and expense, separated them into monthly periods, determine difference of related months, then averages them overall.
    
    def projected_savings():
        #take average savings and project to the end of the financial year.

class expense(budget):
    def __init__(self, name, estimate, actual):
        super().__init__(name, estimate, actual)

class income(budget):
    def __init__(self, name, estimate, actual):
        super().__init__(name, estimate, actual)
    def period_gross():
        #take all income sources and add them together for returning.
    def period_net():
        #take income sources and send them to taxes.py for processing, add together, then return