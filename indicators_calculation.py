#indicators_calculation.py

def calculate_sma(period, list_of_price):
    sum = 0
    if period > len(list_of_price):
        return -1
    for price in list_of_price:
        sum += price
        return sum/len(list_of_price)


#list of price, first index would be the oldest day price
def calculate_ema(period, list_of_price, smoothing, first_day_ema):
    #ema_prev = calculate_sma(list_of_price[20:40])      #first ema will be 20 days sma
    ema_prev = first_day_ema
    ema_current = 0
    offset = smoothing/(1+period)
    if period > len(list_of_price):
        return
    for index in range(list_of_price):
        ema_current = list_of_price[index]*offset + ema_prev*(1-offset)
        ema_prev = ema_current
    return ema_current


def calculate_macd(slow_ma_period, fast_ma_period, signal_period, list_of_price):

    return