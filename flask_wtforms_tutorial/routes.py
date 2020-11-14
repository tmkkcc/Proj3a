from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash, session

from .forms import StockForm
from .charts import *
from .symbolInput import SymbolInput
from .dateInput import DateInput
from .chartTypeInput import ChartTypeInput
from .timeSeriesInput import  TimeSeriesInput
from .dateInput import DateInput




@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    global symbolsCache

    chart = None
    err = None
    smin = SymbolInput()
    try:
        smin.symbols = symbolsCache
        print("The Symbols are being loaded from the cache.")

    except NameError:
        print("Please Wait")
        symbolsCache = smin.loadSymbols()

    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']

            if (smin.isInputValid(symbol) == False):
                err = smin.error

            chart_type = request.form['chart_type']

            ct = ChartTypeInput()
            if(smin.isInputValid(chart_type) == False):
                err = ct.error

            time_series = request.form['time_series']
            ts = TimeSeriesInput()
            if(ts.isInputValid(time_series) == False):
                err =ts.error

            start_date = request.form['start_date']
            #No conversions??
            #Ask them why?

            end_date = request.form['end_date']

            di = DateInput()
            if(di.isInputValid(start_date, end_date) == False):
                err = di.error

            if err == None:
                chart = queryStockData(symbol, chart_type, time_series, start_date, end_date)

                if (chart == "throttled"):
                    chart = None
                    err = "Error, please wait up to a minute"
            #if end_date <= start_date:
                #Generate error message as pass to the page
               # err = "ERROR: End date cannot be earlier than Start date."
              #  chart = None
            #else:
                #query the api using the form data
                #err = None
                 
                #THIS IS WHERE YOU WILL CALL THE METHODS FROM THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE
            
                
                
                
                
                #This chart variable is what is passed to the stock.html page to render the chart returned from the api
                #chart = "ASSIGN CHART TO THIS VARIABLE"

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")
