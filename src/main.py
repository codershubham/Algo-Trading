from indicators import *
from plot import *
from sendmail import *
import time

DEPLOY_DIR_PATH="E:\AlgoTrading\Stock-Market\deploy\list-of-stock"
stock_list = []

def check_trigger_for_buy(stock):
    df = calculate_macd(stock)
    #print(df)
    df_last_2 = df.tail(2)
    # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
    if ( 
            df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] < 0 and 
            df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] > 0 and 
            df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] >  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
        ):
            send_mail(stock)


def load_stocks_list():
    myfile= open( DEPLOY_DIR_PATH, "r" )
    for x in myfile:
        stock_list.append(x.strip())
    myfile.close()


if __name__ == "__main__":
    load_stocks_list() 
    print(stock_list)
    while True:
        for stock in stock_list:
            check_trigger_for_buy(stock)
        time.sleep(60*60*2) 
    #df.to_csv('dataframe.csv')
    #create_plot(df)
