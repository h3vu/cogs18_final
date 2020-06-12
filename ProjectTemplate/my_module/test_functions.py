from alpha_vantage.timeseries import TimeSeries
from my_module.functions import price_change, past_five_minutes, stock_volatility, big_five

def test_price_change():
    assert callable(price_change)
    assert stock_name is str

def test_past_five_minutes():
    assert callable(past_five_minutes)
    assert percent_change_per_minute == price_change(stock_name)
    assert table_of_past_five_minutes != None

def test_stock_variability():
    assert callable(stock_variability)
    assert statement != None
    assert statement == str
    assert stock_volatility(0.02) == 'The stock is volatile.'
    assert stock_volatility(-0.00065) == 'The stock is slightly volatile.'
    assert stock_volatility(0.0001) == 'The stock is not volatile.'

def test_big_five():
    assert callable(big_five)
    assert stock_name is str
    assert big_five('APPL') == 'APL is a stock in the the Big Five! The CEO is Tim Cook.'
    assert big_five('STOR') == 'STOR is not a stock in the Big Five. Please look up the CEO.'
    assert ceo_information != None      