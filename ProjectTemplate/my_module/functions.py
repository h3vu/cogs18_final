from alpha_vantage.timeseries import TimeSeries


# slighly modified function from Derrick Sherrill's on Github
# https://github.com/Derrick-Sherrill/DerrickSherrill.com/blob/master/stocks.py
def price_change(stock_name):
    """Displays data about a particular stock and then creates a table to show how the stock is changed every minute.
    
    Parameters
    ----------
    stock_name: string
        the name of the stock
    
    Returns
    -------
    two data tables: first one displays data about the stock
        second one displays per minute change of closing price of the stock
        """
    
    # this pulls real time stock data in minute intervals for open, high, low, close, and volume values
    ts = TimeSeries(key='M2Y7OWUL7DKF5XW9', output_format = 'pandas')
    data, meta_data = ts.get_intraday(symbol=stock_name, interval='1min', outputsize='full')
    print(stock_name)
    print(data)
    
    # displays the minute by minute change in closing price
    close_data = data['4. close']
    percent_change = close_data.pct_change()
    print(percent_change)

    return percent_change


def past_five_minutes(percent_change_per_minute):
    """Displays data table with percent change in closing price between each minute for the past 5 minutes
    
    Parameters
    ----------
    percent_change_per_minute: data table
        value is the output from the previous function
    
    Returns
    -------
    data table with percent change in closing price between each minute for the past 5 minutes
    """
    
    #create table of percent change in price from minute to  minute and adds a column label
    table_of_past_five_minutes = percent_change_per_minute.head(5)
    table_of_past_five_minutes = table_of_past_five_minutes.rename('percent_change')
    
    return(table_of_past_five_minutes)


def stock_volatility(mean_of_five_minutes):
    """Classifies the volatility of the stock based on the past 5 minutes of data.
    
    Parameters
    ----------
    mean_of_five_minutes: float
        value is the output of past_five_minutes function for the stock of choice
    
    Returns
    -------
    statement: string
        statement of stock's votility based on percent changes of stock in last 5 minutes
    
    """
    
    print(mean_of_five_minutes)
    
    if abs(mean_of_five_minutes) > 0.001:
        statement = 'The stock is volatile.'
    elif abs(mean_of_five_minutes) > 0.0005 and abs(mean_of_five_minutes) < 0.001:
        statement = 'The stock is slightly volatile.'
    elif abs(mean_of_five_minutes) < 0.0005:
        statement = 'The stock is not volatile.'
   
    print('Average Percentage Change Over Past 5 Minutes:')
    print(mean_of_five_minutes)
    print(statement)

    return statement


def big_five(stock_name):
    """Identify if the stock of choice is in the Big Five, and if it is, gives the CEO's name.
    
    Parameters
    ----------
    stock_name: string
        
    Returns
    -------
    ceo_information: string
    
    """
    
    #this stores the name of the CEO for the Big Five companies
    big_five_ceo = {
    'AAPL': 'Tim Cook',
    'FB': 'Mark Zuckerberg',
    'GOOGL':' Sundar Pichai',
    'MSFT': 'Satya Nadella',
    'AMZN': 'Jeff Benzos'}
    
    # statement based on if the the stock is one of the Big Five companies
    if stock_name in big_five_ceo:
        ceo_information = stock_name + ' is a stock in the the Big Five! The CEO is ' + big_five_ceo[stock_name] + '.'
    else:
        ceo_information = stock_name + ' is not a stock in the Big Five. Please look up the CEO.'
    
    print(ceo_information)
    
    return ceo_information
