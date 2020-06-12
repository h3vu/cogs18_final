from alpha_vantage.timeseries import TimeSeries
from my_module.functions import price_change, past_five_minutes, stock_volatility, big_five

stock_name = 'STOR'

price_change('STOR')
#percent_change_per_minute = price_change(stock_name)

past_five_minutes(percent_change_per_minute)
print(past_five_minutes(percent_change_per_minute))
mean_of_five_minutes = past_five_minutes(percent_change_per_minute).mean()

stock_volatility(mean_of_five_minutes)

big_five(stock_name)