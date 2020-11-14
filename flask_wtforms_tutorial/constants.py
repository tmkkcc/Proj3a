class Constants:
    # Use constants so specfic user input type can be referenced globally without magic strings everywhere.
    SYMBOL = "symbol"
    CHARTTYPE = "chartType"
    SERIES = "series"
    STARTDATE = "startDate"
    ENDDATE = "endDate"
    SYMBOL_SEARCH = "SYMBOL_SEARCH"
    API_URL = "https://www.alphavantage.co/query"
    API_KEY = "SPFP6JN8KMDZ9IPM"

    CHARTTYPES = {
        "1": "Bar",
        "2": "Line"
    }

    TIMESERIES = {
        "1": "Intraday",
        "2": "Daily",
        "3": "Weekly",
        "4": "Monthly"
    }
