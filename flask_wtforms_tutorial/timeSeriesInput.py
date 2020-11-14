import requests
#Time Series Function Input
class TimeSeriesInput():
    def __init__(self):
        """Chart Type input constructor"""
        self.error = None

    def isInputValid(self, time_series):
        try:
            selection = int(time_series)
            if(selection < 1 or selection > 4):
                self.error = "Please select one of the four options for the time series."
                print(self.error)
                return False
        except ValueError:
            self.error = "Please select one of the four options for the time series."
            print(self.error)
            return False

        print(time_series)
        return True

    
