from .charts import convert_date
import requests

class DateInput():
    def __init__(self):
        self.error = None

    def isInputValid(self, start_date, end_date):
        #validate start date
        try:
            start = convert_date(start_date)
        except ValueError:
            self.error = "Invalid start date provided."
            return False
        
        #validate end date
        try:
            end = convert_date(end_date)
        except ValueError:
            self.error = "Invalid end date provided."
            return False
        
        #error handling for end date before start date
        if start >= end:
            self.error = "End date must be after start date"
            return False

        # Date is valid
        return True