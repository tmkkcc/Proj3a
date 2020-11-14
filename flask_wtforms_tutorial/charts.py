'''
This web service extends the Alphavantage api by creating a visualization module,
converting json query results retuned from the api into charts and other graphics.

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime, date
from .constants import Constants
from .stockModel import StockModel
import pygal


# Helper function for converting date
def convert_date(str_date):
    if (str_date.find(" ") == -1):
        return datetime.strptime(str_date, '%Y-%m-%d').date()
    else:
        return convert_datetime(str_date)


def convert_datetime(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S').date()


def queryStockData(symbol, chart_type, time_series, start_date, end_date):
    """ Given a set of inputs performs a stock query """

    # API Query paramters
    series = "TIME_SERIES_" + Constants.TIMESERIES[time_series].upper()
    data = {
        "function": series,
        "symbol": symbol,
        "outputsize": "full",
        "interval": "60min",
        "apikey": Constants.API_KEY
    }

    print(data)

    # Sending our request to the API using the information we put in the data collection.
    apiCall = requests.get(Constants.API_URL, params=data)

    # Stores the json-enconded content in the retrieved data.
    response = apiCall.json()

    if (response.__contains__('Note')):
        # We hit a throttling limit; just return an error and wait.
        return "throttled"

    # If statements to change key depending on the Time Serires selected.
    if series == "TIME_SERIES_INTRADAY":
        timeSeries = "Time Series (60min)"
    elif series == "TIME_SERIES_DAILY":
        timeSeries = "Time Series (Daily)"
    elif series == "TIME_SERIES_WEEKLY":
        timeSeries = "Weekly Time Series"
    elif series == "TIME_SERIES_MONTHLY":
        timeSeries = "Monthly Time Series"

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []

    # Parsing the dates from the user input
    startDate = convert_date(start_date)
    endDate = convert_date(end_date)

    items = list(response[timeSeries].items())
    i = len(items) - 1
    while i >= 0:
        date, stockData = items[i]

        # Parsing the date from the api record.
        entryDate = convert_date(date)

        # Populating lists with data, within the given date range, from API
        if (entryDate >= startDate and entryDate <= endDate):
            model = StockModel(stockData)
            opens.append(model.open)
            highs.append(model.high)
            lows.append(model.low)
            closes.append(model.close)
            dates.append(date)

        i = i - 1

    # If true, prints line chart. Else prints the bar chart.
    if (chart_type == "1"):
        chart = pygal.Bar(x_label_rotation=45)
    else:
        chart = pygal.Line(x_label_rotation=45)

    chart.x_labels = dates
    chart.title = "Stock Date for " + symbol + ": " + start_date + " to " + end_date
    chart.add("Open", opens)
    chart.add("High", highs)
    chart.add("Low", lows)
    chart.add("Close", closes)

    return chart.render_data_uri()