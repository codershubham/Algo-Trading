from indicators import *
from plot import *
from sendmail import *
import time
import sys


HOLDINGS_PATH="E:\AlgoTrading\Stock-Market\deploy\list-of-holdings"
WATCHLIST_PATH="E:\AlgoTrading\Stock-Market\deploy\\watchlist"
EXPORTED_FILES_DIR_PATH="E:\AlgoTrading\Stock-Market\\tests\\"
holdings_list = []
watchlist = []
DEBUG_MODE = False
SEND_NOTIFICATION=True

def check_trigger_for_buy(stock):
    print("stock", stock)
    df = calculate_macd(stock)
    df_last_2 = df.tail(2)
    # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
    if ( 
            df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] < 0 and 
            df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] > 0 and 
            df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] >  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
        ):
        return 1
    else:
        return 0


def check_trigger_for_sell(stock):
    df = calculate_macd(stock)
    #print(df)
    df_last_2 = df.tail(2)
    # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
    if (
            df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] > 0 and
            df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] < 0 and
            df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] <  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
        ):
        return 1
    else:
        return 0


def load_stocks_list():
    print("loading holdings : ")
    myfile= open( HOLDINGS_PATH, "r" )
    for x in myfile:
        holdings_list.append(x.strip())
    myfile.close()

    print("loading watchlist : ")
    myfile= open( WATCHLIST_PATH, "r" )
    for x in myfile:
        watchlist.append(x.strip())
    myfile.close()


if __name__ == "__main__":
    if DEBUG_MODE:
        # By default it is FAZE3AUTO.BO, change it to debug
        #df = yf.Ticker('FAZE3AUTO.BO').history(period='1y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
        #df.to_csv(EXPORTED_FILES_DIR_PATH + 'faze2auto.csv')
        #sys.exit()
        calculate_heikin_ashi("RELIANCE.NS")

    load_stocks_list() 
    print(holdings_list)
    while True:
        print("scanning stocks in holding list")
        messege_buy = ''
        messege_sell = ''
        for stock in holdings_list:
            print(stock)
            messege_buy = "List of stocks to buy from holdings:-\n"
            messege_sell = "List of stocks to sell from holdings:-\n"
            try:
                if check_trigger_for_buy(stock):
                    messege_buy += stock + "\n"
                if check_trigger_for_sell(stock):
                    messege_sell += stock + "\n"
            except IndexError:
                print("Data for " + stock + " doesn't exist")
            except Exception as ex:
                print("some error occured", ex)

        if SEND_NOTIFICATION: 
            send_mail(messege_buy)
            send_mail(messege_sell)

        print("scanning stocks in watchlist")
        messege_buy = ''
        messege_sell = ''
        for stock in watchlist:
            print(stock)
            messege_buy = "List of stocks to buy from watchlists :-\n"
            messege_sell = "List of stocks to sell from watchlists :-\n"
            try:
                if check_trigger_for_buy(stock):
                    messege_buy += stock + "\n"
                if check_trigger_for_sell(stock):
                    messege_sell += stock + "\n"
            except IndexError:
                print("Data for " + stock + " doesn't exist")
            except Exception as ex:
                print("some error occured", ex)

        if SEND_NOTIFICATION:
            send_mail(messege_buy)
            send_mail(messege_sell)

        time.sleep(60*60*24) 
    #create_plot(df)
