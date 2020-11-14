import requests

class ChartTypeInput():
    
    def __init__(self):
        """Chart Type input constructor"""
        self.error = None
      
      
    def isInputValid(self, chart_type):
        
        print(chart_type)
        if (chart_type == "1"):
            return True
        elif (chart_type == "2"):
            return True
        else:
            self.error = "User didn't select 1 or 2"
            return False

