from flask import current_app
import requests 
from .constants import Constants

class SymbolInput():

    def __init__(self):
        """Symbol input constructor"""
        self.error = None
        self.symbols = None

    def isInputValid(self, symbol):
        """The shared validate input function."""
        # Query paramaters
        data = {
            "function":Constants.SYMBOL_SEARCH,
            "keywords":symbol,
            "apikey":Constants.API_KEY
        }

        # Query symbol search API
        print("making api call.")
        apiCall = requests.get(Constants.API_URL, params=data)
        response = apiCall.json()
        print("made api call.")

        # for each returned match 
        matches = []
        for match in response["bestMatches"]:
            # if an exact match symbol is valid; return true
            if(match["1. symbol"].upper() == symbol.upper()):
                return True
            else:
                matches.append(match["1. symbol"])
            
        # if not an exact match, display best matches from the api
        self.error = f'{symbol} was not found. Did you mean {", ".join(matches)}?'
        print(self.error)
        return False

    def loadSymbols(self):
        symbols = []
        with current_app.open_resource('listing_status.csv', 'r') as f:
            skip = True
            for line in f:
                if (skip):
                    skip = False
                    continue
                crumbs = line.split(',', 1)
                symbolTuple = (crumbs[0], crumbs[0])
                symbols.append(symbolTuple)
            
            self.symbols = symbols
        return symbols



