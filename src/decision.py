from indicators import *
from logger import *


logObject = Logger.getObject("decision").logger
def check_trigger_for_buy(list_of_stock):
    result = []
    for stock in list_of_stock:
        print(stock)
        try:
            df = calculate_macd(stock)
            df_last_2 = df.tail(2)
            # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
            if ( 
                    df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] < 0 and 
                    df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] > 0 and 
                    df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] >  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
                ):
                result.append(stock)
        except IndexError:
            logObject.error("Data for " + stock + " doesn't exist")
        except Exception as ex:
            print("some error occured", ex)
    return result
   


def check_trigger_for_sell(list_of_stock):
    result = []
    for stock in list_of_stock:
        print(stock)
        try:
            df = calculate_macd(stock)
            #print(df)
            df_last_2 = df.tail(2)
            # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
            if (
                    df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] > 0 and
                    df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] < 0 and
                    df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] <  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
                ):
                result.append(stock)
        except IndexError:
            logObject.error("Data for " + stock + " doesn't exist")
        except Exception as ex:
            print("some error occured", ex)
    return result
